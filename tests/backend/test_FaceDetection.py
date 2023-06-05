import pytest
from backend.FaceDetection import FaceDetection
import numpy as np

dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)


@pytest.fixture
def face_detection():
    return FaceDetection()


def test_detect_face_mtcnn(face_detection):

    result = face_detection.detect_face_mtcnn(dummy_image)

    assert isinstance(result, np.ndarray)
    assert result.shape == (100, 100, 3)


def test_detect_face_dlib(face_detection):

    result = face_detection.detect_face_dlib(dummy_image)

    assert isinstance(result, np.ndarray)
    assert result.shape == (100, 100, 3)
