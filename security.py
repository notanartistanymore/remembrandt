import bcrypt
from jose import JWTError, jwt
from fastapi import HTTPException

from datetime import datetime, timedelta, timezone

from config import settings


def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password=password.encode(encoding="utf-8"), salt=bcrypt.gensalt()
    ).decode(encoding="utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password=password.encode(encoding="utf-8"),
        hashed_password=hashed_password.encode(encoding="utf-8"),
    )


def create_access_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")


def decode_access_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        return int(payload["sub"])
    except (JWTError, KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token")
