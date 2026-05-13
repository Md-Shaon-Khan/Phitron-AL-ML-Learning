import streamlit as st 
import pandas as pd

data = {
  "Name":["Alice","Bob","Charlie"],
  "Age":[25,30,35],
  "City":["New York","London","Paris"]
}

df = pd.DataFrame(data)
st.write("### Using st.write() for DataFrame")
st.write(df)

st.table(df)
st.dataframe(df)

person = {
  "Name":"Shaon Khan",
  "Age":25,
  "Skills":["Python","Streamlit","Data Science"]
}

st.json(person)
st.write("Dictionary displayed with st.write(): ",person)

editable_df = st.data_editor(df, num_rows="dynamic")
st.write("Updated DataFrame: ")
st.write(editable_df)