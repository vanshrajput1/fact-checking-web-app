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
    search = tavily.search(
    f"latest real-time data {claim}",
    max_results=5
)


    prompt = f"""
You are a professional fact-checking system.

Rules:
- Use ONLY reliable, real-time web sources from the evidence provided.
- If the claim is outdated, speculative, or unsupported, classify it as False.
- When correcting a claim, give the latest confirmed value.
- If the claim involves a numeric value (price, percentage, amount), you MUST provide the latest confirmed real-time value if available.
- For conceptual claims, provide a brief explanation and at least one credible source instead of "Not applicable".
Output format:

<Verified:| Inaccurate: | False:>
<Correct real-time information or "Not applicable">
Sources: <Comma-separated source names>

Do NOT put multiple fields on the same line.
Do NOT add extra text.



Claim:
{claim}

Web Evidence:
{search}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

