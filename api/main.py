from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from util_funcs import convert_image_to_array
from FaceDetection import FaceDetection
import cv2



class TaskIn(BaseModel):
    my_string: str


class TaskOut(BaseModel):
    message: str


app = FastAPI()
detector = FaceDetection(model="Dlib")

@app.get('/')
async def get_root():
    return "Welcome to my Python API!!!"


@app.post('/task', response_model=TaskOut)
async def do_task(request: TaskIn):
    my_string = request.my_string


    return {"message": my_string}


@app.post('/faceDetection')
async def do_task(image_file: UploadFile = File(...)):

    contents = await image_file.read()

    image = convert_image_to_array(contents)

    new_image = detector.detect_dlib(image=image)
    
    print(new_image)
    cv2.imwrite('test_dlib2.jpg', new_image)
    return {"message": "Success"}