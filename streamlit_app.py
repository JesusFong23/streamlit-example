from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

def explore_data(file_path):
    # Read in the CSV file using Pandas
    data = pd.read_csv(file_path)
    
    # Return the DataFrame
    return data

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
    
#Referencias Jcharis and ChatGPT
