import numpy as np
import cv2


def convert_image_to_array(contents: bytes) -> np.ndarray:
    """
    Convert image bytes to cv2 image
    """
    nparr = np.frombuffer(contents, np.uint8)
    cv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return cv_image
