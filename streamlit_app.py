from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(30, 5),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)
