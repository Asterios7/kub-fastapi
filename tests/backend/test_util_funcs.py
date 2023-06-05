import cv2
import numpy
from backend.util_funcs import (decode_image,
                                encode_image)


image = cv2.imread('tests/data/test_image.jpg')
_, img_bytes = cv2.imencode('.jpg', image)
image_bytes= img_bytes.tobytes()


def test_decode_image():
    decoded_image = decode_image(image_bytes)
    assert type(decoded_image) == numpy.ndarray


def test_encode_image():
    encoded_image = encode_image(image)
    assert type(encoded_image) == bytes