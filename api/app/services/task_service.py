from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.task import Task, TaskPriority, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, owner_id: int, payload: TaskCreate) -> Task:
    task = Task(**payload.model_dump(), owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def list_tasks(
    db: Session,
    owner_id: int,
    skip: int,
    limit: int,
    status: TaskStatus | None = None,
    priority: TaskPriority | None = None,
    search: str | None = None,
) -> tuple[list[Task], int]:
    filters = [Task.owner_id == owner_id]
    if status:
        filters.append(Task.status == status)
    if priority:
        filters.append(Task.priority == priority)
    if search:
        filters.append(Task.title.ilike(f"%{search}%"))

    stmt = select(Task).where(*filters).order_by(Task.created_at.desc()).offset(skip).limit(limit)
    count_stmt = select(func.count(Task.id)).where(*filters)

    items = db.execute(stmt).scalars().all()
    total = db.execute(count_stmt).scalar_one()
    return items, total


def get_task(db: Session, owner_id: int, task_id: int) -> Task | None:
    stmt = select(Task).where(Task.id == task_id, Task.owner_id == owner_id)
    return db.execute(stmt).scalar_one_or_none()


def update_task(db: Session, task: Task, payload: TaskUpdate) -> Task:
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()
