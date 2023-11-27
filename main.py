import streamlit as st
from app import connect, show
from PIL import Image

import os
import pandas as pd

title = 'מטבחסן'

st.title(title)

data = show()
# Initialize an empty list to store rows
rows = []

# Iterate through the data list
for product in data:
    # Create a row with the product's information
    row = [
        st.image(product['picture'], width=100, caption=product['name']),
        st.write(product['amount'])
    ]

    # Append the row to the list of rows
    rows.append(row)

# Create a single table using the list of rows
st.table(rows)


def handle_upload():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

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
