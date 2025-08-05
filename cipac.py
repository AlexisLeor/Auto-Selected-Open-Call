import requests
from bs4 import BeautifulSoup
from utils import make_id

def scrape_cipac():
    url = "https://cipac.net/annonces/appels"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = []
    for item in soup.select(".views-row"):
        titre = item.select_one(".title").text.strip()
        lien = item.select_one("a")["href"]
        deadline = "Non précisée"
        results.append({
            "id": make_id(titre, lien),
            "titre": titre,
            "lien": lien,
            "deadline": deadline,
            "localisation": "France",
            "niveau": "emerging",
            "tags": "professionnel",
            "chance": "moyenne",
            "commentaire": "Appel listé par le CIPAC",
            "international": False
        })
    return results
