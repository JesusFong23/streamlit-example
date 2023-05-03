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

conn = st.experimental_connection("databasedating.sql")
df = conn.query("select * from FIRST_NAME ")
st.dataframe(df)
