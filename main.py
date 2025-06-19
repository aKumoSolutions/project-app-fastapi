from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class UserData(BaseModel):
    name: str
    age: int

class ListDirInput(BaseModel):
    path: str

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
        files = os.listdir(path.path)  
        return {"files": files} 
    except:
        return{"There is some error, try again"}

# Jonathan's Task
@app.get("/get_public_ip")
def get_ip():
    try:
        pub_ip = requests.get('https://api.ipify.org')
        pub_ip = pub_ip.text
        return {"message": f"Your public IP address is: {pub_ip}"}
    except:
        return {"message": "Error fetching public IP"}
        
