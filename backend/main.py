from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from util_funcs import decode_image, encode_image
from FaceDetection import FaceDetection
import io


class TaskIn(BaseModel):
    my_string: str


class TaskOut(BaseModel):
    message: str


class Image(BaseModel):
    format: str = Field(..., description="Image format (e.g., JPEG, PNG)")
    data: bytes = Field(..., description="Image data as bytes")


class FaceDetectionOut(BaseModel):
    image: Image


app = FastAPI()
detector = FaceDetection()

@app.get('/')
async def get_root():
    return "Welcome to my Python API!!!"


@app.post('/task', response_model=TaskOut)
async def do_task(request: TaskIn):
    my_string = request.my_string

    return {"message": my_string}


@app.post('/faceDetection', response_model=FaceDetectionOut)
async def do_task(image_file: UploadFile = File(...)):

    contents = await image_file.read()

    image = decode_image(contents)

    boxed_image = detector.detect_face_dlib(image=image)
    boxed_image_bytes = encode_image(boxed_image)

    return StreamingResponse(io.BytesIO(boxed_image_bytes), 
                             media_type="image/jpeg")