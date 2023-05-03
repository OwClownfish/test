import streamlit as st
import pandas as pd
import numpy as np

st.title('DCI test app')

df = pd.read_csv('https://github.com/OwClownfish/test/blob/main/mockdata.csv')
st.table(df)