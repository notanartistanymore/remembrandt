import bcrypt


def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password=password.encode(encoding="utf-8"), salt=bcrypt.gensalt()
    ).decode(encoding="utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password=password.encode(encoding="utf-8"),
        hashed_password=hashed_password.encode(encoding="utf-8"),
    )
