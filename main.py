from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

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
        
# Naza's Task - read_log_tail(filepath, lines)
@app.get("/read_log_tail(filepath, lines)")
def read_log_tail(filepath: str, lines: int = 5):
    try:
        # this opens the file for reading. "r" means read.
        file = open(filepath, "r") 
        content = file.readlines()
        last_lines = content[-lines:]
        return {"lines": last_lines}
    except FileNotFoundError:
        return {"error": "File not found. Check the path."}
