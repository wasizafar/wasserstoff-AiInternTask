import streamlit as st
import sqlite3
import pandas as pd
import subprocess
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.services.email_reply import generate_reply_by_gemini, generate_reply_by_groq # AI Reply Generator
from src.services.email_sender import send_email #email sending function
from src.services.email_cleaner import clean_email_body #emial cleaner fromt the html tags

DB_PATH = r"data\emails.db"
VENV_PATH = os.path.join("myenv", "Scripts", "activate")  # Windows path for venv activation

@st.cache_resource #handle catch resourse
def get_emails():
    """Fetch stored emails from the database."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM emails ORDER BY date DESC LIMIT 30", conn)
    conn.close()
    return df

def fetch_new_emails():
    # Run emial_fetcher.py using the current Python environment.
    subprocess.run([sys.executable, r"src\services\email_fetcher.py"], check=True)

# Streamlit UI
st.set_page_config(page_title="AI Email Assistant", layout="wide")

st.title("📧 AI-Powered Email Assistant")
st.write("Displaying fetched emails from Gmail")

#  Button to fetch new emails
if st.button("Fetch New Emails"):
    with st.spinner("Fetching emails...."):
        fetch_new_emails()
    st.success("Emails fetch sucessfully!")
    st.rerun()

# Load emails from DB
emails = get_emails()

if emails.empty:
    st.warning("No emails found in the database. Run the email fetcher script first.")
else:
    # Show emails in a table
    st.dataframe(emails, height=400, use_container_width=True)

    # Select email to view details
    email_subjects = emails["subject"].tolist()
    selected_email = st.selectbox("Select an email:", email_subjects)

    # Display selected email details
    email_data = emails[emails["subject"] == selected_email].iloc[0]

    st.subheader("📜 Email Details")
    st.write(f"**Subject:** {email_data['subject']}")
    st.write(f"**From:** {email_data['sender']}")
    st.write(f"**To:** {email_data['recipient']}")
    st.write(f"**Date:** {email_data['date']}")
    st.write("**Body:**")
    with st.expander("Body"):
        st.info(email_data["body"])
    # st.text_area('Body', email_data['body'])
    
    option = st.selectbox(
            "Choose one of these AI model",
            ('Gemini AI', 'Groq AI'),
            index=None,
            placeholder="choose the AI Model"
        )

    #clean emial body with gemini
    if st.button("clean & summarize Email"):
        with st.spinner("cleaning email content..."):
            clea_body = clean_email_body(email_data['body'])
        st.subheader("cleaned email content")
        st.info(clea_body)

        # Generate AI Reply using Gemini
    # make option to choose the AI  Model
    if st.button("Generate AI Reply"):
        # with st.popover('Choose the AI Model'):
        if option == "Gemini AI":
            try:
                with st.spinner("Generating reply using Gemini AI...."):
                    ai_reply = generate_reply_by_gemini(email_data['subject'], email_data['body'])
                st.subheader("AI-Generated Reply")
                reply_text = st.text_area('Edit before sending:', ai_reply, height=200)
            except Exception as e:
                st.warning(f"⚠️ Gemini AI API error: {e}")

        elif option == 'Groq AI':
            try:
                with st.spinner('Generating reply using Groq AI....'):
                    ai_reply = generate_reply_by_groq(email_data['subject'], email_data['body'], email_data['sender'],email_data['recipient'])
                st.subheader('AI-Generated Reply')
                reply_text = st.text_area('Edit before sending:', ai_reply, height=200)
            except Exception as e:
                st.warning(f"⚠️ Groq AI API error: {e}")
        else:
            st.warning("Please select an AI model before generating a reply.")


        # Send Email Button
        if st.button("Send Reply"):
            with st.spinner("Sending email...."):
                success = send_email(email_data['sender'], email_data['subject'], reply_text)
            if success:
                st.success("Email sent sucessfully!")
            else:
                st.error("Failed to send email. Check STMP settings.")

    else:
        st.subheader("Raw Email Body")
        st.code(email_data['body'][:3000], language="html")
        # Generate AI Reply using Gemini
    # if st.button("Generate AI Reply"):
    #     with st.spinner("Generating reply using Gemini AI...."):
    #         ai_reply = generate_reply(email_data['subject'], email_data['body'])
    #     st.subheader("AI-Generated Reply")
    #     reply_text = st.text_area('Edit before sending:', ai_reply, height=200)

    #     # Send Email Button
    #     if st.button("Send Reply"):
    #         with st.spinner("Sending email...."):
    #             success = send_email(email_data['sender'], email_data['subject'], reply_text)
    #         if success:
    #             st.success("Email sent sucessfully!")
    #         else:
    #             st.error("Failed to send email. Check STMP settings.")

    
