import streamlit as st 

st.title("My First APP")
st.write("Hello World")

st.header("Section 1")
st.write("This is a simple section")


import pandas as pd

st.title("Display Example")

st.write("Hello Streamlit")
st.write(100)
st.write([1, 2, 3, 4, 5])

st.write(({"name":"Shaon Khan","age":21}))

df =  pd.DataFrame({
  "Name":['A','B','C'],
  "Marks":[80,90,85]
})

st.write(df)


st.write(42)

st.markdown("**Bold Text** and _italic_")

name = "Shaon Khan"

name



st.title("Amar Health APP")

st.header("Rogir Tottho")
st.subheader("Bektigoto Biboron")
st.text("Plain text")
st.caption("* Sokol tottho gopon thakbe.")