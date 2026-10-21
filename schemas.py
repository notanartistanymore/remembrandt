from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    task_title: str
    task_done: bool = False


class TaskUpdateRequest(BaseModel):
    task_title: str | None = None
    task_done: bool | None = None


class TaskCreateResponse(TaskCreateRequest):
    task_id: int
