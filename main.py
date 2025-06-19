from fastapi import FastAPI
from pydantic import BaseModel
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

@app.get('/generate_uuid/')
def generate_uuid():
    try:
        generated_uuid = uuid4()
        return {"message": f"Your UUID is: {generated_uuid}"}
    except:
        return {"message": "Error generating UUID"}