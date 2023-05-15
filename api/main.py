from fastapi import FastAPI
from pydantic import BaseModel


class TaskIn(BaseModel):
    my_string: str


class TaskOut(BaseModel):
    message: str


app = FastAPI()

@app.get('/')
async def get_root():
    return "Welcome to my Python API!!!"


@app.post('/task', response_model=TaskOut)
async def do_task(request: TaskIn):
    my_string = request.my_string

    return {"message": my_string}