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

```
ai-email-assistant/
├── .env                      # API keys and credentials
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── frontend/
│   └── app.py                # Streamlit web app
├── src/
│   ├── services/
│   │   ├── email_fetcher.py  # Fetches emails via IMAP
│   │   ├── email_cleaner.py  # Summarizes HTML emails via Gemini
│   │   ├── email_reply.py    # Generates smart replies
│   │   └── email_sender.py   # Sends emails using SMTP
│   └── utils/
│       └── db.py             # DB connection + helpers
├── data/
│   └── emails.db             # Local SQLite database
└── .gitignore                # Ignore unnecessary files
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-email-assistant.git
cd ai-email-assistant
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate     # Windows
# OR
source myenv/bin/activate    # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your `.env` File

Create a `.env` file in the root with the following content:

```env
# Gemini API Key
GEMINI_API_KEY=your_gemini_api_key

# Gmail IMAP/SMTP
EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your_app_password
IMAP_SERVER=imap.gmail.com

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=youremail@gmail.com
SMTP_PASSWORD=your_app_password
```

> ⚠️ Use an [App Password](https://myaccount.google.com/apppasswords) if using Gmail with 2FA enabled.

---

## ▶️ Running the App

```bash
streamlit run frontend/app.py
```

Then open in browser (usually at `http://localhost:8501`).

---

## 🧪 How It Works

1. **Fetch Emails** using the "Fetch New Emails" button.
2. Select an email to **Clean & Summarize** its content via Gemini API.
3. Click **Generate Reply** to get a context-aware draft.
4. Hit **Send Reply** to email the response to the sender.

---

## 🧾 Example Use Case

- A messy email with lots of HTML tags is received.
- The AI cleans it up to summarize it neatly.
- You click "Generate Reply" and get a complete response draft.
- Click "Send" — it's delivered via Gmail.

---

## 🔐 Security

- `.env` holds all secrets — never commit this file!
- `.gitignore` excludes credentials, `emails.db`, venv, and logs.

---

## 📌 Future Features

- 🔔 Slack notification integration
- 📅 Google Calendar scheduling
- 🧠 Conversation thread-aware replies
- 🌐 Web search integration

---

## 📝 License

MIT License

---

## 👏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [Google Gmail API](https://developers.google.com/gmail/api)