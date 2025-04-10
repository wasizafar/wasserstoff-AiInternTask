import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def generate_reply(email_subject, email_body):
    """Generates an AI-powered reply for an email using Google's Gemini API."""
    
    prompt = f"""
    You are an AI email assistant. Read the following email and generate a professional reply.

    Subject: {email_subject}
    Body: {email_body}

    Your reply should be clear, concise, and professional.
    """
    
    model = genai.GenerativeModel("gemini-pro")  # Use Gemini-Pro model
    response = model.generate_content(prompt)

    return response.text.strip()
