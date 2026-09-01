from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")

# In-memory data keeps the focus on API design instead of database setup.
tasks = [
    {"id": 1, "title": "Read the FastAPI documentation", "completed": False},
    {"id": 2, "title": "Build a REST endpoint", "completed": True},
]


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


@app.get("/tasks")
def get_tasks():
    """Return all tasks."""
    # TODO: Return the tasks list.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Return one task by ID."""
    # TODO: Find the task, or raise HTTPException with status 404.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Create and return a new task."""
    # TODO: Build a new task with the next available ID and append it to tasks.
    pass
