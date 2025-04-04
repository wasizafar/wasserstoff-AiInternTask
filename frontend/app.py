import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "data/emails.db"

def get_emails():
    """Fetch stored emails from the database."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM emails ORDER BY date DESC", conn)
    conn.close()
    return df

# Streamlit UI
st.set_page_config(page_title="AI Email Assistant", layout="wide")

st.title("📧 AI-Powered Email Assistant")
st.write("Displaying fetched emails from Gmail")

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
    st.info(email_data["body"])
