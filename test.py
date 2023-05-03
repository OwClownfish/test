import streamlit as st
import pandas as pd
import numpy as np

st.title('DCI test app')

DATA_URL = ('https://github.com/OwClownfish/test/blob/main/mockdata.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data = load_data(10000)
st.write(data)