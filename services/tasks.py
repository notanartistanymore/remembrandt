from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.tasks import TaskRepository
from schemas import TaskCreateRequest, TaskUpdateRequest


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def list(self, task_done: bool | None):
        return self.repo.list(task_done=task_done)

    def get_or_404(self, task_id: int):
        task = self.repo.get_by_id_or_none(task_id=task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def create(self, payload: TaskCreateRequest):
        return self.repo.create(
            task_title=payload.task_title, task_done=payload.task_done
        )

    def update(self, task_id: int, payload: TaskUpdateRequest):
        task = self.repo.get_by_id_or_none(task_id)
        if payload.task_title is not None:
            task.task_title = payload.task_title
        if payload.task_done is not None:
            task.task_done = payload.task_done
        return self.repo.save(task)

    def delete(self, task_id: int):
        task = self.repo.get_by_id_or_none(task_id)
        return self.repo.delete(task)
