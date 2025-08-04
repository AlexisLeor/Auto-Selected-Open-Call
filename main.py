import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("OPENAI_API_KEY")  # ou "BREVO_API_KEY" si tu l’as appelée comme ça dans Render
EMAIL_FROM = os.getenv("MAIL_USER")
EMAIL_TO = os.getenv("DEST_EMAIL")

def send_email_via_brevo(subject, html_content):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }
    data = {
        "sender": {"name": "Veille artistique", "email": EMAIL_FROM},
        "to": [{"email": EMAIL_TO}],
        "subject": subject,
        "htmlContent": html_content
    }
    r = requests.post(url, headers=headers, json=data)
    print("Email sent:", r.status_code, r.text)

if __name__ == "__main__":
    send_email_via_brevo("Test Veille", "<h1>Ceci est un test</h1><p>Le script fonctionne bien via Brevo.</p>")
