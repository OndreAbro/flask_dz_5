from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Task(BaseModel):
    title: str
    description: str
    status: int


tasks = []


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < len(tasks):
        return tasks[task_id]
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < len(tasks):
        tasks[task_id] = task
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        del tasks[task_id]
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


# POST-запрос в Windows
# curl -X "POST" "http://localhost:8000/tasks" -H "Content-Type: application/json" -d "{\"title\": \"Task example\", \"description\": \"Description of the task\", \"status\": 0}"