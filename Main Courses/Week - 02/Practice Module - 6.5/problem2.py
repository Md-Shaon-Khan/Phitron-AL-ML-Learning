
import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["api_key"])
model = genai.GenerativeModel("gemini-3-flash-preview")

st.set_page_config(page_title="Gemini Chatbot", page_icon="✨")
st.title("✨ Gemini AI Chat")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Ask Gemini anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Build context
                history = ""
                for msg in st.session_state.messages:
                    role = "User" if msg["role"] == "user" else "Assistant"
                    history += f"{role}: {msg['content']}\n"

                response = model.generate_content(history)
                reply = response.text if response.text else "⚠️ Empty response."

            except Exception as e:
                reply = f"❌ Error: {str(e)}"

            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})