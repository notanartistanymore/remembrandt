from fastapi import FastAPI

from routes.tasks import router as tasks_router
from routes.auth import router as auth_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Remembrandt App")

app.include_router(router=tasks_router, tags=["tasks"])
app.include_router(router=auth_router, tags=["auth"])
