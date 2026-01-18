import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=get_gemini_key()
)

def extract_claims(text):
    prompt = f"""
Extract factual claims from the text.

Rules:
- ONLY extract claims that contain numbers, dates, prices, percentages, or measurable quantities.
- IGNORE descriptive, editorial, or meta statements (for example, statements about what the report provides or discusses).
- Each claim must be a single sentence copied exactly from the text.
- Do NOT rephrase or explain anything.
- If a sentence does not contain a checkable fact, ignore it.

Examples:

Input: "The Eiffel Tower is 500 meters tall."
Output:
The Eiffel Tower is 500 meters tall.

Input: "This report provides a Q1 2026 outlook."
Output:
(no output)

Input: "As of January 2026, Bitcoin is trading at $42,500."
Output:
As of January 2026, Bitcoin is trading at $42,500.

Text:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.split("\n")
