import streamlit as st 
import pandas as pd


data = {
  "rogir nam":['Shaon','Ayan','Shahadat'],
  'boyos':[22, 9, 23],
  'rog': ['Diabetes','High Pressure','Normal']
}

df = pd.DataFrame(data)

st.dataframe(df)
st.table(df)
st.write(df)

st.json({"Name":"Shaon","Project":"HealthBridge"})

data = {
  "Name":["A","B","C"],
  "Marks":[80, 90, 85]
}

df = pd.DataFrame(data)

st.dataframe(data)
st.table(df)


st.metric(label="Heart Rate", value="75 BPM",delta="+5")
st.metric(label="Good",value="Average",delta="-One step ahead")

st.metric("Heart Rate","75 BPM","0")