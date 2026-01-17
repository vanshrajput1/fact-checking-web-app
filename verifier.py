import streamlit as st
from google import genai
from tavily import TavilyClient

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

tavily = TavilyClient(
    api_key=st.secrets["TAVILY_API_KEY"]
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
