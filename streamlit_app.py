from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
