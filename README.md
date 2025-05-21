# 📬 AI-Powered Email Assistant

An intelligent personal assistant that connects to your Gmail inbox, fetches emails, cleans HTML-heavy content using Gemini AI, generates context-aware replies, and sends them — all through a sleek Streamlit interface.

---

## 🚀 Features

- 🔐 **Secure Gmail Integration** via IMAP
- 🧠 **AI-Powered Email Cleaning** using **Gemini API**
- ✍️ **Auto-Generated Smart Replies**
- 📤 **Send Replies via Gmail SMTP**
- 📊 **Streamlit Web App UI** to manage and interact with your inbox
- 🗃️ **SQLite Database** to store and retrieve email threads

---

## 🧰 Tools & Frameworks Used

| Tool / Library       | Purpose                                     |
|----------------------|---------------------------------------------|
| Python 3.8+          | Core backend logic                          |
| Streamlit            | Web user interface                          |
| Google Gemini API    | Cleaning and replying using LLM             |
| IMAP (imaplib)       | Fetching emails                             |
| SMTP (smtplib)       | Sending replies                             |
| SQLite               | Lightweight local database                  |
| python-dotenv        | Secure config management                    |
| pandas               | Tabular data handling                       |

---

## 📁 Project Structure

'''
ai-email-assistant/
├── .env                   # Environment variables (API keys, credentials)
├── README.md              # Project overview and setup instructions
├── requirements.txt       # List of Python dependencies
├── frontend/
│   └── app.py             # Streamlit web application
├── src/
│   ├── services/
│   │   ├── email_fetcher.py   # Fetches emails via IMAP
│   │   ├── email_cleaner.py   # Cleans and summarizes HTML emails using Gemini API
│   │   ├── email_reply.py     # Generates intelligent email replies
│   │   └── email_sender.py    # Sends email responses using SMTP
│   └── utils/
│       └── db.py              # Handles SQLite DB connection and helpers
├── data/
│   └── emails.db          # Local SQLite database for storing emails
└── .gitignore             # Specifies files and folders to ignore in version control
'''
---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-email-assistant.git
cd ai-email-assistant

