from google import genai
from dotenv import load_dotenv
import os
import io

load_dotenv()

client = genai.Client(api_key=os.getenv("CODE_DEBUGGER"))

def solution_master(images, selected_option):

    prompt = f"""
You are an expert AI programming debugger.

Analyze the uploaded code screenshot(s) carefully.

USER OPTION: {selected_option}

If "Hints":
- Give only step-by-step hints
- No full code

If "Solution":
- Give full fixed code + explanation

FORMAT:
### Error Summary
### Reason
### Response
"""

    image_parts = []

    for img in images:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        image_parts.append(buf.getvalue())
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt, *images]
    )

    return response.text