import streamlit as st
from backend_requests import post_request_faceDetector

st.title("Face Detection")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image file was uploaded
if uploaded_file is not None:
    # Read the contents of the image file
    image = uploaded_file.read()
    
    # Display the uploaded image
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption='Uploaded Image')

    boxed_image = post_request_faceDetector(image=image)

    with col2:
        st.image(boxed_image, caption='Boxed Image')
