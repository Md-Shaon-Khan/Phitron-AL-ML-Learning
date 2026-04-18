import streamlit as st 

with st.container():
  st.write("This is inside a container")

col1, col2 = st.columns(2)

with col1:
  st.write("Column 1 content")
  st.write("Shaon")
with col2:
  st.write("Column 2 content")
  st.write("Khan")

with st.expander("More info"):
  st.write("Hidden content revealed when expanded")

option = st.sidebar.selectbox("Select page:",['Home','Settings','About'])
st.sidebar.write("Sidebar content here")

st.write(f"Current Page: {option}")
st.divider()

st.caption("This is a small caption text below")