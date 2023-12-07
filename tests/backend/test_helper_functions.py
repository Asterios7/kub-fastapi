from PIL import Image
from backend.helper_functions import draw_face_boxes
from dlib_wrapper import dlibFaceProcessor
import numpy as np

image = Image.open('tests/data/test_image.jpg')

face_processor = dlibFaceProcessor()
faces = face_processor.detect_faces(np.array(image))

def test_draw_face_boxes():
    img_byte_array = draw_face_boxes(image, faces)
    assert isinstance(img_byte_array, bytes)
