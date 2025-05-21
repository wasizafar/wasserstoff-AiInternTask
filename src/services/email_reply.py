import google.generativeai as genai
import os
from dotenv import load_dotenv
from groq import Groq
import requests # for the use of groq API

load_dotenv()  # Load API key from .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# GROK_API_KEY = os.getenv("GROK_API_KEY")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
client = Groq(
    api_key = os.getenv("GROK_API_KEY"),
)

def generate_reply_by_gemini(email_subject, email_body):
    """Generates an AI-powered reply for an email using Google's Gemini API."""
    
    prompt = f"""
    You are an AI email assistant. Read the following email and generate a professional reply.

    Subject: {email_subject}
    Body: {email_body}

    Your reply should be clear, concise, and professional.
    """
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use Gemini-Pro model
    response = model.generate_content(prompt)

    return response.text.strip()

def generate_reply_by_groq(email_subject, email_body, sender_name, reciver_name):
    """Generates an AI-powered reply for an email using Google's Gemini API."""
    # cunstruct the prompt
    prompt = f"""You are an AI email assistant. Read the following email and generate a professional reply.
    my name : {reciver_name.split('<')[0]}
    sender's name : {sender_name.split('<')[0]}
    Subject: {email_subject}
    Body: {email_body}

    Your reply should be clear, concise, and professional.
    """
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