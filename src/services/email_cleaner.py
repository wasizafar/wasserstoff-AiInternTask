import google.generativeai as genai
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
client = Groq(
    api_key = os.getenv("GROK_API_KEY"),
)

def clean_email_body_by_gemini(html_body):
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

def clean_email_body_by_groq(html_body):
    """Uses Groq to clean and summarize email content that may be in HTML format."""
    # cunstruct the prompt
    prompt = f"""The following is an HTML email. Please remove HTML tags, extract the meaningful content,
    and provide a clean, human-readable summary of the message.

    HTML Email:
    {html_body}
    """
    try:
        # send request to groq chat complation API
        chat_completion = client.chat.completions.create(
            messages = [
                {"role": "system", "content": "You are an AI email assistant."},
                {"role": "user", "content": prompt}
            ],
            model = "meta-llama/llama-4-scout-17b-16e-instruct",
            stream = False
        )
        return chat_completion.choices[0].message.content.strip()
    except:
        print(f"Groq cleaning failed: {e}")
        return "could not clean email content"

    
    