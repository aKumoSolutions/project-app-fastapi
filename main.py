from fastapi import FastAPI
from pydantic import BaseModel
import platform
import subprocess
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

@app.post("/ping_host")
 # Pings a host to check for reachability. Returns True if reachable, False otherwise.
def ping_host(hostname: str) -> bool:
    try:
        # -n for Windows, -c for Linux/macOS.
        if platform.system().lower() == 'windows':
            param = '-n'
        else:
            param = '-c'
        command = ['ping', param, '1', hostname]
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        result.returncode == 0:
    except Exception as e:
        print(f"An error occurred in ping_host for '{hostname}': {e}")
        return False

# Jonathan's Task
@app.get("/get_public_ip")
def get_ip():
    try:
        pub_ip = requests.get('https://api.ipify.org')
        pub_ip = pub_ip.text
        return {"message": f"Your public IP address is: {pub_ip}"}
    except:
        return {"message": "Error fetching public IP"}
       
