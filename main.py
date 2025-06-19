from fastapi import FastAPI
from pydantic import BaseModel
import requests

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

# Jonathan's Task
@app.get("/get_public_ip")
def get_ip():
    try:
        pub_ip = requests.get('https://api.ipify.org')
        pub_ip = pub_ip.text
        return {"message": f"Your public IP address is: {pub_ip}"}
    except:
        return {"message": "Error fetching public IP"}
# Tugs's task
@app.get("/cpuLoadAverage")
def cpu_t():
    try:
        load_ave = os.getloadavg()
        print(f"Cpu load average last 1 minutes, 5 minutes, 15 minutes: {load_ave}")
        return f"Cpu load average last 1 minutes, 5 minutes, 15 minutes: {load_ave}"
    except:
        print("Try again")
        return "it should be good"        
