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

st.title("Dating App")

my_dataset = "databasedating.csv"

# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
	data = explore_data("databasedating.csv")
	st.dataframe(data)

# Show Description
if st.checkbox("Show All Column Name"):
	data = explore_data("databasedating.csv")
	st.text("Columns:")
	st.write(data.columns)

# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
if data_dim == 'Rows':
	data = explore_data("databasedating.csv")
	st.text("Showing Length of Rows")
	st.write(len(data))
if data_dim == 'Columns':
	data = explore_data("databasedating.csv")
	st.text("Showing Length of Columns")
	st.write(data.shape[1])


if st.checkbox("Show Summary of Dataset"):
	data = explore_data("databasedating.csv")
	st.write(data.describe())
