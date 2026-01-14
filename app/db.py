from uuid import uuid4
from datetime import datetime

# Local in-memory storage (simulating DynamoDB)
TASKS_DB = {}

def create_task(data):
    task_id = str(uuid4())
    task = {
        "task_id": task_id,
        "title": data["title"],
        "description": data["description"],
        "status": data.get("status", "Pending"),
        "created_at": datetime.utcnow().isoformat()
    }
    TASKS_DB[task_id] = task
    return task
def get_all_tasks():
    return list(TASKS_DB.values())
def get_task_by_id(task_id):
    return TASKS_DB.get(task_id)
def update_task_status(task_id, status):
    if task_id in TASKS_DB:
        TASKS_DB[task_id]["status"] = status
        return TASKS_DB[task_id]
    return None
def delete_task(task_id):
    return TASKS_DB.pop(task_id, None)
