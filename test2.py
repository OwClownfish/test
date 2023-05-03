import streamlit as st
import datetime
from pandas import read_csv
import pandas as pd
import numpy as np
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
st.title('DCI test app help50')

uploaded_file = st.file_uploader('Upload a CSV')
    # Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)

try:
    st.write(dataframe)

    #def parser(x):
    # return datetime.strptime('190'+x, '%Y-%m')
    #fig = pyplot.figure()
    #fig.suptitle('matplotlib.pyplot.show() Example')
    #series = read_csv(dataframe, header=0, parse_dates=[0], index_col=0, date_parser=parser)
    #series.index = series.index.to_period('M')
    # fit model
    #model = ARIMA(series, order=(5,1,0))
    #model_fit = model.fit()
    #series.plot()
    #pyplot.show()
    #st.pyplot(fig)
    st.line_chart(dataframe)
except:
    pass

