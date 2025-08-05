import requests
from bs4 import BeautifulSoup
from utils import make_id

def scrape_cnap():
    results = []
    base_url = "https://www.cnap.fr/annonces?page="
    page = 0
    while True:
        r = requests.get(base_url + str(page))
        soup = BeautifulSoup(r.text, "html.parser")
        items = soup.select(".annonce-item")
        if not items:
            break
        for item in items:
            titre = item.select_one("h3").text.strip()
            lien = "https://www.cnap.fr" + item.select_one("a")["href"]
            deadline = item.select_one(".date").text.strip() if item.select_one(".date") else "Non précisée"
            results.append({
                "id": make_id(titre, lien),
                "titre": titre,
                "lien": lien,
                "deadline": deadline,
                "localisation": "France",
                "niveau": "emerging",
                "tags": "public, institutionnel",
                "chance": "élevée",
                "commentaire": "Appel à projet via le CNAP",
                "international": False
            })
        page += 1
    return results
