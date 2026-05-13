import streamlit as st 

st.title(":world_map: Input your Information", anchor=False)

st.divider()

name = st.text_input("Enter your name baby: ",placeholder="Your name...",)

print(type(name))
st.write(f"Your name is: {name}")

st.divider()

age = st.number_input("Enter your age", value=None,placeholder="Type your age...")

print(type(age))
st.write(f"Your age is: {age}")

password = st.text_input("Enter your password: ",placeholder="Be safe",type="password")

print(type(password))
st.write(f"Your password is: {password}")

pressed = st.button("Enter to confirm.", type="primary")

if pressed:
  st.write(f"Your name is {name} and your age is {age}")

selected = st.selectbox("Choose your profession",
             ("Student","Employee","Teacher"),index=None,
             accept_new_options=True)

print(type(selected))

st.write(f"You selected {selected}")









