# # import streamlit as st

# # st.chat_message("user").write("Hello")
# # st.chat_message("assistant").write("Hi there!")

# # msg = st.chat_input("Type a message")

# # if msg:
# #     st.write(msg)

# # message = st.text_input("Hello")

# import streamlit as st

# st.title("Simple Chat")

# user_input = st.chat_input("Say something")

# if user_input:
#     st.chat_message("user").write(user_input)
#     st.chat_message("assistant").write("You said: " + user_input)
    
# msg = st.chat_input("Ask about ECG")

# if msg:
#     st.chat_message("assistant").write("Analyzing ECG...")


import streamlit as st

# Chat history রাখতে session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# আগের messages দেখাও
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input নাও
prompt = st.chat_input("জিজ্ঞেস করো...")
if prompt:
    # User message দেখাও
    with st.chat_message("user"):
        st.write(prompt)
    # AI reply দাও
    with st.chat_message("assistant"):
        st.write("আমি তোমার HealthBridge AI!")