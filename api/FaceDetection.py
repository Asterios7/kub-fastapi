from deepface import DeepFace
from mtcnn.mtcnn import MTCNN
from deepface.detectors import FaceDetector
import numpy as np
import cv2


class FaceDetection:
    def __init__(self) -> None:
        pass

    def detect_mtcnn(self, image: np.ndarray) -> np.ndarray:

        detector = MTCNN()
        faces = detector.detect_faces(image)

        for face in faces:
            x, y, width, height = face['box']
            # Save the image with bounding boxes
            image = cv2.rectangle(image, (x, y),
                                  (x+width, y+height),
                                  (0, 255, 0), 2)

        return image

    def detect_dlib(self, image: np.ndarray) -> np.ndarray:

        detector = FaceDetector.build_model('dlib')
        faces = FaceDetector.detect_faces(detector, 'dlib', image)

        for face in faces:
            (x, y, width, height) = face[1]
            # Save the image with bounding boxes
            image = cv2.rectangle(image, (x, y),
                                  (x + width, y + height),
                                  (255, 0, 0), 2)

        return image
