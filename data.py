import streamlit as st
from app import connect, show
from PIL import Image


def page1():
    data = show()
    for product in data:
        st.image(product['picture'], width=100, caption=product['name']),
        st.write(product['amount'])


def page2():
    st.write("this is page 1 ")


def page3():
    st.write("This is the page 3 ")


def page4():
    st.write("This is the page 4 ")


def page5():
    st.write("This is the page 5 ")


st.sidebar.title("My app  !")
st.sidebar.markdown("")

page = st.sidebar.selectbox("תפריט", ["הצג הכל", "אוסף", "חיפוש", "עדכן", "מחק"])
st.title("מטבחסן")
if page == "הצג הכל":
    page1()

elif page == "אוסף":
    page2()
elif page == "חיפוש":
    page3()
elif page == "עדכן":
    page4()
else:
    page5()
