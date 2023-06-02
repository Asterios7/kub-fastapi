from deepface import DeepFace
from mtcnn.mtcnn import MTCNN
from retinaface import RetinaFace
from deepface.detectors import FaceDetector
import numpy as np
import cv2


class FaceDetection:
    def __init__(self, model: str) -> None:
        self.detectors = ["opencv", "ssd", "mtcnn", "retinaface"]
        self.encoders = ["VGG-Face", "Facenet", "OpenFace",
                         "DeepFace", "DeepID", "ArcFace", "Dlib"]
        self.model = model

        pass

    def detect_mtcnn(self, image: np.ndarray) -> list:

        detector = MTCNN()
        faces = detector.detect_faces(image)

        for face in faces:
            x, y, width, height = face['box']
            # Save the image with bounding boxes
            cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)
            cv2.imwrite('test_mtcnn.jpg', image)


    def detect_dlib(self, image: np.ndarray) -> list:

        detector = FaceDetector.build_model('dlib')
        faces = FaceDetector.detect_faces(detector, 'dlib', image)

        for face in faces:
            (x, y, w, h) = face[1]
            # Save the image with bounding boxes
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imwrite('test_dlib.jpg', image)
            
        
        return image