import pytest
from fastapi.testclient import TestClient
from PIL import Image
from io import BytesIO
import sys
sys.path.append("./backend")
from backend.main import app

client = TestClient(app)


@pytest.mark.parametrize("image_path, status_code", 
                         [('tests/data/test_image.jpg', 200)])
def test_detect_face(image_path, status_code):
    # Create a sample image file
    image = Image.open(image_path)

    # Convert the image to bytes
    image_bytes = BytesIO()
    image.save(image_bytes, format='JPEG')
    example_image_bytes = image_bytes.getvalue()

    response = client.post("/detect_face", 
                           files={"image_file": example_image_bytes})

    assert response.status_code == status_code
    assert response.headers["content-type"] == "image/jpeg"
