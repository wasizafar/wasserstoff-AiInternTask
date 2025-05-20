import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def clean_email_body(html_body):
    """
    Uses Gemini to clean and summarize email content that may be in HTML format.
    """
    prompt = f"""
    The following is an HTML email. Please remove HTML tags, extract the meaningful content,
    and provide a clean, human-readable summary of the message.

    HTML Email:
    {html_body}
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini cleaning failed: {e}")
        return "could not clean email content"
    