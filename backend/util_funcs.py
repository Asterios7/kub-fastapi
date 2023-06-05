import numpy as np
import cv2


def decode_image(contents: bytes) -> np.ndarray:
    """
    Convert image bytes to cv2 image
    """
    nparr = np.frombuffer(contents, np.uint8)
    cv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return cv_image


def encode_image(image: np.ndarray) -> bytes:
    """
    Convert cv2 image to image bytes
    """
    _, img_bytes = cv2.imencode('.jpg', image)
    return img_bytes.tobytes()
