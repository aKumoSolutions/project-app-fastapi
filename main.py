from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserData(BaseModel):
    name: str
    age: int

@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}

@app.post("/hello")
def create_user(user: UserData):
    print(user.name, user.age)
    return {"message": f"Hello, {user.name}!"}

# check_disk_usage(path) Meerim

import shutil
import os

@app.post("/disk-usage/")

def check_disk_usage(data: PathRequest):
    path = data.path
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Path does not exist")
    total, used, free = shutil.disk_usage(path)
    return {
        "path": path,
        "total_GB": round(total / (2**30), 2),
        "used_GB": round(used / (2**30), 2),
        "free_GB": round(free / (2**30), 2)
        }