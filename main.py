import streamlit as st
from app import connect, show
from PIL import Image

import os
import pandas as pd

title = 'מטבחסן'

st.title(title)


def handle_upload():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    data = show()
    for product in data:
        #st.write(product['name'])
        st.image(product['picture'], width=100, caption=product['name'])
        st.write(product['amount'])


    if uploaded_file:
        image_bit = uploaded_file.read()
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        name = st.text_input("What the name of the product")
        amount = st.number_input('Enter a amount ', 0)

        if st.button("Save Data"):
            # Make sure the directory exists
            connect(name, image_bit, amount)

            st.success('Data Save')


handle_upload()
