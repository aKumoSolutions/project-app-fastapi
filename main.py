from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
import shutil

app = FastAPI()

class UserData(BaseModel):
    name: str
    age: int

class ListDirInput(BaseModel):
    input: str

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
        
# Meerim's task  check_disk_usage(path)

@app.get("/disk-usage/")
def check_disk_usage(path: str):
    try:
        total, used, free = shutil.disk_usage(path)
        return {
            "path": path,
            "total_GB": round(total / (2**30), 2),
            "used_GB": round(used / (2**30), 2),
            "free_GB": round(free / (2**30), 2)
        }
    except FileNotFoundError:
        return {"error": "Path does not exist"}