import streamlit as st
import datetime
from pandas import read_csv
import pandas as pd
import numpy as np
from matplotlib import pyplot
st.title('DCI test app help32')

uploaded_file = st.file_uploader('Upload a CSV')
    # Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)



 
def parser(x):
 return datetime.strptime('190'+x, '%Y-%m')
 
series = read_csv(dataframe, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
test = series.plot()
pyplot.show()
#
st.pyplot(test)
