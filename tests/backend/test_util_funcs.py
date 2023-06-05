import cv2
import numpy as np
from backend.util_funcs import (decode_image,
                                encode_image)


image = cv2.imread('tests/data/test_image.jpg')
_, img_bytes = cv2.imencode('.jpg', image)
image_bytes= img_bytes.tobytes()


def test_decode_image():
    result = decode_image(image_bytes)
    assert isinstance(result, np.ndarray)


def test_encode_image():
    result = encode_image(image)
    assert isinstance(result, bytes)