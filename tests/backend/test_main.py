import pytest
from fastapi.testclient import TestClient
from backend.main import app
import cv2

client = TestClient(app)


@pytest.mark.parametrize("image_path, status_code", [
    ('tests/data/test_image.jpg', 200)])


def test_detect_face(image_path, status_code):
    
    # Create a sample image file
    image = cv2.imread(image_path)
    _, img_bytes = cv2.imencode('.jpg', image)
    image_file = img_bytes.tobytes()

    response = client.post("/faceDetection", files={"image_file": image_file})

    # Perform assertions on the response
    assert response.status_code == status_code
    assert response.headers["content-type"] == "image/jpeg"

