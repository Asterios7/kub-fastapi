from locust import HttpUser, task, tag, between
from PIL import Image
import io

HOST = "http://localhost:8000"

# Open image and convert to bytes
image = Image.open('./tests/data/test_image.jpg') 
image_bytes = io.BytesIO()
image.save(image_bytes, format='JPEG')
example_image_bytes = image_bytes.getvalue()

class MyUser(HttpUser):
    wait_time = between(2, 5)

    @tag("get_root")
    @task
    def get_root(self):
        url = HOST + '/'
        self.client.get(url)

    @tag("detect_face")
    @task
    def detect_face_request(self):
        url = HOST + '/detect_face'
        self.client.post(url, files={'image_file': example_image_bytes})


