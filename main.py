from fastapi import FastAPI
from pydantic import BaseModel
import requests
from uuid import uuid4

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

# Yunus's task
@app.get('/generate_uuid/')
def generate_uuid():
    try:
        generated_uuid = uuid4()
        return {"message": f"Your UUID is: {generated_uuid}"}
    except:
        return {"message": "Error generating UUID"}

# Jonathan's Task
@app.get("/get_public_ip")
def get_ip():
    try:
        pub_ip = requests.get('https://api.ipify.org')
        pub_ip = pub_ip.text
        return {"message": f"Your public IP address is: {pub_ip}"}
    except:
        return {"message": "Error fetching public IP"}
        