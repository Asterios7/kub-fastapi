import requests
import os

IP_ADDRESS = os.environ.get('BACKEND_ADDRESS')


def post_request_faceDetector(image: bytes):

    url = f'http://{IP_ADDRESS}/faceDetection'

    # Send the POST request with the player name and image file
    response = requests.post(url,
                             files={'image_file': image})

    # Check the response
    if response.status_code == 200:
        print('Request successful.')
        return response.content
    else:
        print('Error:', response.text)
        return response
