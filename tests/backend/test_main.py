from fastapi.testclient import TestClient
from backend.main import app
import cv2

client = TestClient(app)

def test_detect_face():
    

    # Create a sample image file
    image = cv2.imread('tests/data/test_image.jpg')
    _, img_bytes = cv2.imencode('.jpg', image)
    image_file = img_bytes.tobytes()

    response = client.post("/faceDetection", files={"image_file": image_file})

    # Perform assertions on the response
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

    # Check the content of the response
    # received_image_data = response.content
    # ... Perform additional assertions on the received_image_data if needed