from fastapi import HTTPException

import models
from schemas import UserCreateRequest
from security import hash_password, verify_password, create_access_token
from repositories.users import UserRepository


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, payload: UserCreateRequest):
        if self.repo.get_by_email(payload.email) is not None:
            raise HTTPException(status_code=409, detail="Email already registered")
        return self.repo.create(
            email=payload.email, password_hash=hash_password(payload.password)
        )

    def authenticate(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if user is None or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=404, detail="Invalid credentials")
        return {
            "access_token": create_access_token(user_id=user.user_id),
            "token_type": "bearer",
        }
