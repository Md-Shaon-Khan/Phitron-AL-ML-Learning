import streamlit as st 
import pandas as pd
import numpy as np

data = np.random.randn(50, 1)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 15])
st.pyplot(fig)


data = pd.DataFrame(np.random.randn(50, 1),
                    columns=["ECG Signal"])

st.line_chart(data)


scores = pd.DataFrame({
  "Rog":[0.85, 0.72, 0.91]
}, index=['Diabetes','Heart','Normal'])

st.bar_chart(scores)