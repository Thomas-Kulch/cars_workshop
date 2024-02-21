import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

from data import unique_manufacturer

st.header('Market of Used Cars')
st.write('Filter the data below to see the ads by manufacturer.')

st.selectbox('Select a Manufacturer', unique_manufacturer)