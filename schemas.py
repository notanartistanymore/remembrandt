from pydantic import BaseModel, EmailStr


class TaskCreateRequest(BaseModel):
    task_title: str
    task_done: bool = False


class TaskUpdateRequest(BaseModel):
    task_title: str | None = None
    task_done: bool | None = None


class TaskCreateResponse(TaskCreateRequest):
    task_id: int


class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str


class UserCreateResponse(BaseModel):
    user_id: int
    email: EmailStr


class TokenOutResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
