import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
