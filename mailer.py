import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

def send_email(nouveaux, rappels):
    subject = "🎯 Veille artistique — Nouveaux appels à projets"
    html_content = "<h1>Nouveaux appels</h1><ul>"
    for call in nouveaux:
        html_content += f"<li>{call}</li><br>"
    html_content += "</ul><hr><h2>Rappels</h2><ul>"
    for call in rappels:
        html_content += f"<li>{call}</li><br>"
    html_content += "</ul>"

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

    r = requests.post("https://api.brevo.com/v3/smtp/email", headers=headers, json=data)
    print("Email sent:", r.status_code, r.text)
