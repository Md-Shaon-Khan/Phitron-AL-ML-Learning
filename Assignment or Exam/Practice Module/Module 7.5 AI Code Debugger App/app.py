import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image
from solution import solution_master
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(override=True)

groq_client = Groq(api_key=os.getenv("GROQ_API_CHAT"))

if "debug_response" not in st.session_state:
    st.session_state.debug_response = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Shaon Code Debugger App")
st.divider()

with st.sidebar.container():
    images = st.file_uploader("Upload your error's code...", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    pil_images = []

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    length = len(images)
    if images:
        if length > 2:
            st.error("Shaon can accept maximum 2 images only.")
        else:
            cols = st.columns(length)
            for i in range(length):
                with cols[i]:
                    st.image(images[i])

    selected_option = st.selectbox("What you want...", ('Hints', 'Solution'), index=None)

    pressed = st.button("Submit", type="secondary")


if pressed:
    if not images:
        st.error("You have to upload at least one image")
    if not selected_option:
        st.error("You have to select either Hints or Solution")

    if images and selected_option:
        with st.container(border=True):
            st.header(f"Your {selected_option} provided by Shaon Sir")

        with st.spinner("Shaon is following your command, please wait..."):
            generate_solution = solution_master(pil_images, selected_option)
            st.session_state.debug_response = generate_solution
            st.markdown(generate_solution)


if st.session_state.debug_response:

    st.divider()
    st.subheader("Chat with AI (Groq)")

    user_query = st.text_input("Ask follow-up question")

    if st.button("Ask AI"):

        if user_query:

            with st.spinner("Groq is thinking..."):

                chat_prompt = f"""
You are a helpful programming assistant.

Context (from Gemini analysis):
{st.session_state.debug_response}

User question:
{user_query}

Answer clearly and simply.
"""

                response = groq_client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "user", "content": chat_prompt}
                    ]
                )

                answer = response.choices[0].message.content

                st.session_state.chat_history.append((user_query, answer))


if st.session_state.chat_history:

    st.subheader("Chat History")

    for q, a in st.session_state.chat_history[::-1]:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**AI:** {a}")
        st.divider()