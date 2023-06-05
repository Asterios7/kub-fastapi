import pytest
from backend.FaceDetection import FaceDetection
import cv2
import numpy


@pytest.fixture
def face_detection():
    return FaceDetection()


def test_detect_face_mtcnn(face_detection):
    image = cv2.imread('tests/data/test_image.jpg')
    boxed_image = face_detection.detect_face_mtcnn(image)
    assert type(boxed_image) == numpy.ndarray


def test_detect_face_dlib(face_detection):
    image = cv2.imread('tests/data/test_image.jpg')
    boxed_image = face_detection.detect_face_dlib(image)
    assert type(boxed_image) == numpy.ndarray
