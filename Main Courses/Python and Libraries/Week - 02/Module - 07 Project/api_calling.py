from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import streamlit as st 
import io

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


#Note Generator
def note_generator(images):
  
  prompt = """

      Analyze the provided images and generate a well-structured, formal, and professional note.

      Language Requirement:
      - The final output MUST be written entirely in Bangla (বাংলা)
      - Do NOT use any English words in the final answer unless absolutely necessary (e.g., technical terms)

      Writing Style:
      - No emojis
      - Formal, academic, and professional tone
      - Easy to read, clear, and suitable for students
      - Use simple and understandable language
      - Avoid unnecessary complexity

      Structure (Strictly follow this format):
      1. শিরোনাম (Topic Title)
      2. সংজ্ঞা (Definition)
      3. বিস্তারিত ব্যাখ্যা (Detailed Explanation)
      4. উদাহরণ (Example)
      5. গুরুত্বপূর্ণ পয়েন্ট (Key Points / Summary)

      Additional Instructions:
      - Organize the content in bullet points where necessary
      - Highlight important terms or keywords
      - If multiple concepts are present, separate them clearly
      - Maintain logical flow and clarity
      - Make the note suitable for exam preparation and quick revision
      - Ensure the explanation is neither too short nor unnecessarily long

      Goal:
      The note should help a student easily understand, remember, and revise the topic effectively.

  """
  
  response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents=[images,prompt]
  )
  
  return response.text 


def audio_transcription(text):
  speech = gTTS(text=text, lang='bn', slow=False)

# speech.save("Welcome.mp3")
# gTTS → text কে speech এ convert করে
# BytesIO() → in-memory file
# write_to_fp() → audio buffer-এ write

  audio_buffer = io.BytesIO()
  speech.write_to_fp(audio_buffer)
  return audio_buffer

def quiz_generator(images,difficulty):
    prompt = f"""

      Analyze the provided images and generate a quiz based on the content.

Language Requirement:
- The final output MUST be written entirely in Bangla (বাংলা)
- Do NOT use English in the final answer unless absolutely necessary (e.g., technical terms)

Quiz Style:
- Formal and educational tone
- Suitable for students and exam preparation
- Clear and simple language
- No emojis
- {difficulty}

Quiz Structure:
- Create multiple-choice questions (MCQ)
- Each question must have 4 options by points(A, B, C, D), four points not in same line, line by line
- Clearly indicate the correct answer after each question

Difficulty Level:
- Follow the selected difficulty level (Easy / Medium / Hard)
- Adjust question depth accordingly

Additional Instructions:
- Cover all important concepts from the images
- Do not repeat questions
- Ensure questions test understanding, not just memorization
- Keep questions clear and unambiguous
- Provide answer explanation in 1–2 lines if needed

Goal:
The quiz should help students test their understanding and prepare for exams effectively.

  """
  
    response = client.models.generate_content(
      model = "gemini-3-flash-preview",
      contents=[images,prompt]
    )
    
    return response.text 