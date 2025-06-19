from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from fastapi.responses import HTMLResponse

app = FastAPI()

class UserData(BaseModel):
    name: str
    age: int

@app.get("/", response_class=HTMLResponse)
def homepage():
    return "<h1>Welcome to my app!</h1><p1>Salam aleykum</p1>"

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