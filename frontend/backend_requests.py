import requests

def post_request_faceDetector(image: bytes):

    url = 'http://fastapi-app:8000/faceDetection'

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
