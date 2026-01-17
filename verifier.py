import os
import streamlit as st
from google import genai
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def get_key(name):
    try:
        return st.secrets[name]
    except Exception:
        return os.getenv(name)

client = genai.Client(
    api_key=get_key("GEMINI_API_KEY")
)

tavily = TavilyClient(
    api_key=get_key("TAVILY_API_KEY")
)

def verify_claim(claim):
    search = tavily.search(claim, max_results=5)

    prompt = f"""
    Claim: {claim}

    Web Evidence:
    {search}

    Classify as Verified, Inaccurate, or False.
    Provide correction if needed.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
