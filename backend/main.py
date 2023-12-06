from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from dlib_wrapper import dlibFaceProcessor
from PIL import Image
from io import BytesIO
import numpy as np
from helper_functions import draw_face_boxes


class FaceDetectionResponse(BaseModel):
    format: str = Field(..., description="Image format (e.g., JPEG, PNG)")
    data: bytes = Field(..., description="Image data as bytes")


app = FastAPI()
face_processor = dlibFaceProcessor()


@app.get('/')
async def get_root():
    return "Welcome to my Face Detection API!!!"


@app.post('/detect_face', response_model=FaceDetectionResponse)
async def detect_face(image_file: UploadFile = File(...)):

    contents = await image_file.read()
    img = Image.open(BytesIO(contents)).convert('RGB')
    faces = face_processor.detect_faces(np.array(img))
    img_byte_array = draw_face_boxes(img, faces)

    return StreamingResponse(BytesIO(img_byte_array),
                             media_type="image/jpeg")


