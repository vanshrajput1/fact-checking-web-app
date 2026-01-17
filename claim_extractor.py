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
    Only include statistics, dates, financial numbers.
    Return one claim per line.
    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.split("\n")
