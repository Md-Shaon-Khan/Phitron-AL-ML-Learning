from google import genai
import os
from dotenv import load_dotenv
import streamlit
load_dotenv()

api_key = os.environ.get("GEMINI_API")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Tell me an idea of Gemini API in 100 words"
)

streamlit.markdown(response.text)

# 1.
# from google import genai
# Meaning:
# google → package (library)
# genai → module inside google
# What it does:

# 👉 Gemini API use করার জন্য library import করা হচ্ছে

# 2.
# import os
# Meaning:
# os = Operating System module
# What it does:

# 👉 environment variable access করার জন্য ব্যবহার হয়
# 👉 যেমন .env থেকে API key নেওয়া

# 3.
# from dotenv import load_dotenv
# Meaning:
# dotenv → library
# load_dotenv() → function
# What it does:

# 👉 .env file load করে Python-এ
# 👉 যাতে API key secure রাখা যায়

# 4.
# import streamlit
# Meaning:

# 👉 Streamlit library import করা হচ্ছে

# What it does:

# 👉 UI (web app interface) বানানোর জন্য ব্যবহার হয়

# 5.
# load_dotenv()
# What happens:

# 👉 .env file read করে
# 👉 ভিতরের variables (API key) memory-তে load হয়

# 6.
# api_key = os.environ.get("GEMINI_API")
# Step-by-step:
# os.environ → environment variables store করে
# .get("GEMINI_API") → key retrieve করে
# Meaning:

# 👉 .env থেকে API key নেওয়া হচ্ছে

# Example .env
# GEMINI_API=your_api_key_here
# 7.
# client = genai.Client(api_key=api_key)
# Meaning:

# 👉 Gemini API এর সাথে connection তৈরি করা হচ্ছে

# Simple:
# Client = connector
# API key দিয়ে authenticate করে

# 👉 এখন তুমি Gemini use করতে পারবে

# 8.
# response = client.models.generate_content(
# Meaning:

# 👉 Gemini model কে request পাঠানো হচ্ছে

# 9.
# model="gemini-3-flash-preview",
# Meaning:

# 👉 কোন model use করবে সেটি specify করা

# Notes:
# gemini-3-flash-preview → fast + cheap model
# Good for quick response
# 10.
# contents="Tell me an idea of Gemini API in 100 words"
# Meaning:

# 👉 Prompt (question) পাঠানো হচ্ছে

# 👉 Gemini কে বলা হচ্ছে:
# "একটা idea explain করো"

# 11.
# )

# 👉 Request complete

# 12.
# streamlit.markdown(response.text)
# Step-by-step:
# response.text → Gemini এর output
# streamlit.markdown() → UI তে show করে
# Meaning:

# 👉 Gemini এর answer web page এ display করা হচ্ছে