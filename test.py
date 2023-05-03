import streamlit as st
import pandas as pd
import numpy as np

st.title('DCI test app help')

uploaded_file = st.file_uploader('Upload a CSV')
    # Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)

st.line_chart(dataframe)
st.table(dataframe,x="schorsingen", y="datum")