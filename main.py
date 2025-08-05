import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

SENT_FILE = "sent_calls.txt"

# ========== OUTILS ==========
def already_sent(url):
    if not os.path.exists(SENT_FILE):
        return False
    with open(SENT_FILE, "r") as f:
        return url.strip() in f.read()

def mark_as_sent(url):
    with open(SENT_FILE, "a") as f:
        f.write(url.strip() + "\n")

def send_email(subject, html_content):
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

# ========== SCRAPERS ==========
def scrape_cnap():
    print("Scraping CNAP...")
    base = "https://www.cnap.fr"
    url = f"{base}/annonces?page=0"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = []
    for a in soup.select(".views-row .field-content a"):
        link = base + a['href']
        if not already_sent(link):
            title = a.text.strip()
            results.append({"source": "CNAP", "title": title, "url": link})
    return results

def scrape_cipac():
    print("Scraping CIPAC...")
    url = "https://cipac.net/annonces/appels"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = []
    for a in soup.select(".post-title a"):
        link = a['href'] if a['href'].startswith("http") else "https://cipac.net" + a['href']
        if not already_sent(link):
            title = a.text.strip()
            results.append({"source": "CIPAC", "title": title, "url": link})
    return results

# ========== FILTRES / ANALYSE ==========
def apply_filters(calls):
    filtered = []
    for call in calls:
        title = call["title"].lower()

        # Critères d'exclusion stricts
        if "design" in title or "street art" in title or "danse" in title or "théâtre" in title:
            continue
        if "frais de candidature" in title and not any(x in title for x in ["résidence", "honoraires", "prestigieux"]):
            continue

        # Optionnel / filtre doux
        mid_career = "mid-career" in title or "confirmé" in title
        if mid_career:
            call["note"] = "🟨"
            call["comment"] = "Artiste confirmé requis — profil jeune possible si exceptionnel"
        else:
            call["note"] = "🟩"
            call["comment"] = "Appel cohérent avec profil jeune diplômé"

        filtered.append(call)
    return filtered

# ========== FORMAT EMAIL ==========
def build_email(calls):
    now = datetime.now().strftime("%d/%m/%Y")
    html = f"<h2>Veille artistique – {now}</h2>"

    html += "<h3>🟢 Nouveaux appels</h3><ul>"
    for call in calls:
        html += f"<li>{call['note']} <strong>{call['title']}</strong> (<a href='{call['url']}'>lien</a>)<br>{call['comment']}</li><br>"
    html += "</ul><hr>"

    html += "<h3>🔁 Rappels (déjà envoyés)</h3><ul>"
    if os.path.exists(SENT_FILE):
        with open(SENT_FILE, "r") as f:
            for line in f:
                html += f"<li><a href='{line.strip()}'>{line.strip()}</a></li>"
    html += "</ul>"
    return html

# ========== MAIN ==========
def main():
    nouveaux = scrape_cnap() + scrape_cipac()
    filtrés = apply_filters(nouveaux)

    if filtrés:
        email_html = build_email(filtrés)
        send_email("Veille artistique – Nouveaux appels", email_html)
        for call in filtrés:
            mark_as_sent(call["url"])
    else:
        print("Aucun nouvel appel valide trouvé.")

if __name__ == "__main__":
    main()
