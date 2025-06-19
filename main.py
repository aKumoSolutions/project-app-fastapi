from fastapi import FastAPI
from pydantic import BaseModel
import platform
import subprocess

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
        if result.returncode == 0:
            print(f"SUCCESS: The server '{hostname}' is working fine.")
            return True
        else:
            print(f"FAILURE: The server '{hostname}' is unreachable.")
            return False
    except Exception as e:
        print(f"An error occurred in ping_host for '{hostname}': {e}")
        return False

