import dlib
from io import BytesIO
from PIL import ImageDraw


def draw_face_boxes(img, faces: dlib.rectangles) -> bytes:
    """
    Draw boxes around the faces based on the detected faces
    Returns: image with drawn boxes as byte array
    """
    # Draw bounding boxes around detected faces
    draw = ImageDraw.Draw(img)
    for face in faces:
        left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
        draw.rectangle([left, top, right, bottom], outline="green", width=3)

    # Convert the modified image to bytes in JPEG format
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='JPEG')
    img_byte_array.seek(0)
    return img_byte_array.getvalue()
