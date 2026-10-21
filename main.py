from fastapi import FastAPI

from routes.tasks import router as tasks_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Remembrandt App")

app.include_router(router=tasks_router, tags=["tasks"])
