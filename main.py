from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from typing import Optional
import json
import platform
app = FastAPI()

class UserData(BaseModel):
    name: str
    age: int

class ListDirInput(BaseModel):
    input: str

class TaskData(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    assignee: Optional[str] = None

with open('tasks.json', 'r') as f:
    tasks = json.load(f)
f.close()

@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}

@app.post("/hello")
def create_user(user: UserData):
    print(user.name, user.age)
    return {"message": f"Hello, {user.name}!"}

# Elsu's task
@app.post("/listdir")
def list_dir(path: ListDirInput):
    try:
        files = os.listdir(path.input)  
        return {"files": files} 
    except:
        return {
            "Error": "There is some error, try again"
        }

# Jonathan's Task
@app.get("/get_public_ip")
def get_ip():
    try:
        pub_ip = requests.get('https://api.ipify.org')
        pub_ip = pub_ip.text
        return {"message": f"Your public IP address is: {pub_ip}"}
    except:
        return {"message": "Error fetching public IP"}
        
## abdul's task
@app.get("/tasks")
def list_tasks_data():
    try:
        return [TaskData(**tdata) for tdata in tasks.items()]
    except Exception as e:
        return {"error": str(e)}

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    try:
        task = tasks.get(task_id)
        if not task:
            return {"error": f"Task with id {task_id} not found"}
        return TaskData(**task)
    except Exception as e:
        return {"error": str(e)}

@app.put("/tasks/{task_id}")
def update_task(task_id: str, task: TaskData):
    try:
        if task_id not in tasks:
            return {"error": f"Task with id {task_id} not found"}
        for field, value in task.model_dump().items():
            if value is not None and field != "id":
                tasks[task_id][field] = value
        with open('tasks.json', 'w') as f:
            f.write(json.dumps(tasks))
        return {"message": f"Task with id {task_id} updated successfully", "task": tasks[task_id]}
    except Exception as e:
        return {"error": str(e)}

        # shah's Task
@app.get("/system_info")
def system_information():
    sys_info = {
        'System information':platform.system(),
        'Python Version':platform.python_version(),
        'Architecture': platform.architecture()
    }
    return(sys_info)