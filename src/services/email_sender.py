import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv() # load environment variables

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

def send_email(to_email, subject, body):
    "Sends an email using Gmail SMTP."

    msg = MIMEMultipart()
    msg["From"] = SMTP_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP Server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() # secure connection
        server.login(SMTP_EMAIL, SMTP_PASSWORD) # Login

        #Send email
        server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
    