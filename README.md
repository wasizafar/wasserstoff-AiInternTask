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

ai-email-assistant/
├── .env # API keys and credentials
├── README.md # This file
├── requirements.txt # Python dependencies
├── frontend/
│ └── app.py # Streamlit web app
├── src/
│ ├── services/
│ │ ├── email_fetcher.py # Fetches emails via IMAP
│ │ ├── email_cleaner.py # Summarizes HTML emails via Gemini
│ │ ├── email_reply.py # Generates smart replies
│ │ └── email_sender.py # Sends emails using SMTP
│ └── utils/
│ └── db.py # DB connection + helpers
├── data/
│ └── emails.db # Local SQLite database
└── .gitignore # Ignore unnecessary files


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-email-assistant.git
cd ai-email-assistant

