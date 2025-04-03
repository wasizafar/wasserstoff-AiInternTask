import os
import base64
from email import message_from_bytes
from googleapiclient.errors import HttpError
from gmail_service import authenticate_gmail

def fetch_emails(max_results=5):
    """Fetch recent emails from the Gmail inbox."""
    service = authenticate_gmail()

    try:
        # Get emails from the inbox
        response = service.users().messages().list(userId="me", maxResults=max_results).execute()
        messages = response.get("messages", [])

        email_list = []

        if not messages:
            print("📭 No new emails found.")
            return email_list

        for msg in messages:
            msg_id = msg["id"]
            msg_data = service.users().messages().get(userId="me", id=msg_id, format="raw").execute()

            # Decode email
            raw_email = base64.urlsafe_b64decode(msg_data["raw"])
            email_msg = message_from_bytes(raw_email)

            email_data = {
                "id": msg_id,
                "subject": email_msg["Subject"],
                "from": email_msg["From"],
                "to": email_msg["To"],
                "date": email_msg["Date"],
                "body": get_email_body(email_msg)
            }
            email_list.append(email_data)

        return email_list

    except HttpError as error:
        print(f"❌ An error occurred: {error}")
        return []

def get_email_body(email_msg):
    """Extract plain text body from email, handling missing payloads."""
    if email_msg.is_multipart():
        for part in email_msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                payload = part.get_payload(decode=True)
                return payload.decode("utf-8", errors="ignore") if payload else "[No Content]"
            
    # Handle emails without multipart structure
    payload = email_msg.get_payload(decode=True)
    return payload.decode("utf-8", errors="ignore") if payload else "[No Content]"

# Test fetching emails
if __name__ == "__main__":
    emails = fetch_emails(5)
    for email in emails:
        print(f"📩 {email['subject']} from {email['from']}")