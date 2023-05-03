import streamlit as st
import pandas as pd
import numpy as np

st.title('DCI test app')

st.file_uploader('Upload a CSV')

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
st.line_chart(df)
st.table(df)