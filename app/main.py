from fastapi import FastAPI, HTTPException
from app.models import Task
from app.db import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task_status,
    delete_task
)




app = FastAPI(title="Student Task Management API")

@app.post("/task", status_code=201)
def create_task_api(task: Task):
    if not task.title or not task.description:
        raise HTTPException(status_code=400, detail="Missing required fields")

    return create_task(task.dict())
@app.get("/tasks")
def get_tasks():
    return get_all_tasks()
@app.get("/task/{task_id}")
def get_task(task_id: str):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
@app.put("/task/{task_id}")
def update_task(task_id: str, status: str):
    task = update_task_status(task_id, status)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
@app.delete("/task/{task_id}")
def delete_task_api(task_id: str):
    task = delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

