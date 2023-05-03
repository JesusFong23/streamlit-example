from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

"""
# Welcome to Connection Cafe!

Where you can matcha with someone ;)

and create a brew-tiful relationship :heart:
"""
image = Image.open('Green and Violet Y2k Party Stickers Dating Static Snapchat Snap Ad.jpg')

st.image(image, caption='Prototype')

conn = st.experimental_connection("db-1copy.sql")
n = st.slider("Pick a number")
if st.button("Add the number!"):
    with conn.session as session:
        session.execute("INSERT INTO numbers (val) VALUES (:n);", {"n": n})
        session.commit()
