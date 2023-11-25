import streamlit as st
from PIL import Image
import os
import pandas as pd

title = 'מטבחסן'

st.title(title)


def handle_upload():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        name = st.text_input("What the name of the product")
        amount = st.number_input('Enter a amount ', 0)

        if st.button("Save Data"):
            # Make sure the directory exists
            os.makedirs('Images', exist_ok=True)

            image_filename = f'{uploaded_file.name}'
            image_path = os.path.join('Images', image_filename)
            image.save(image_path)
            st.success('Data Save')
            return [name, uploaded_file.name, amount]
    return None


handle_upload()
