import streamlit as st
import pandas as pd
import numpy as np

st.title('DCI test app')

df = pd.read_csv('mockdata.csv')
st.table(df)