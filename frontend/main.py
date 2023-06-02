import streamlit as st
from backend_requests import post_request_faceDetector

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image file was uploaded
if uploaded_file is not None:
    # Read the contents of the image file
    image = uploaded_file.read()
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image')

    boxed_image = post_request_faceDetector(image=image)

st.image(boxed_image, caption='Boxed Image')
