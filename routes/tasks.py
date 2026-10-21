from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import TaskCreateRequest, TaskUpdateRequest, TaskCreateResponse
from database import get_db
import models
from services.tasks import TaskService
from repositories.tasks import TaskRepository

router = APIRouter()


def get_task_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)


def get_task_service(
    repo: TaskRepository = Depends(get_task_repository),
) -> TaskService:
    return TaskService(repo=repo)


@router.get("/tasks", response_model=list[TaskCreateResponse])
def get_tasks(
    task_done: bool | None = None, service: TaskService = Depends(get_task_service)
):
    return service.list(task_done=task_done)


@router.get("/tasks/{task_id}", response_model=TaskCreateResponse)
def get_task_by_id(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.get_or_404(task_id=task_id)


@router.post("/tasks", response_model=TaskCreateResponse, status_code=201)
def add_task(
    payload: TaskCreateRequest, service: TaskService = Depends(get_task_service)
):
    return service.create(payload)


@router.patch("/tasks/{task_id}")
def update_task(
    task_id: int,
    payload: TaskUpdateRequest,
    service: TaskService = Depends(get_task_service),
):
    return service.update(task_id, payload)


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.delete(task_id)
