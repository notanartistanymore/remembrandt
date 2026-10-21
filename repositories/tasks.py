from sqlalchemy.orm import Session

import models


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, task_done: bool | None) -> list[models.Task]:
        query = self.db.query(models.Task)
        if task_done is not None:
            query = query.filter(models.Task.task_done == task_done)
        return query.all()

    def get_by_id_or_none(self, task_id: int) -> models.Task | None:
        return self.db.get(models.Task, task_id)

    def create(self, task_title: str, task_done: bool) -> models.Task:
        task = models.Task(task_title=task_title, task_done=task_done)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def save(self, task: models.Task) -> models.Task:
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: models.Task) -> None:
        self.db.delete(task)
        self.db.commit()
