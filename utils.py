import os
import hashlib

DB_FILE = "sent_ids.txt"

def load_previously_sent_ids():
    if not os.path.exists(DB_FILE):
        return set()
    with open(DB_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())

def save_sent_ids(call_ids):
    with open(DB_FILE, "a") as f:
        for id_ in call_ids:
            f.write(f"{id_}\n")

def is_relevant_call(call):
    if "frais" in call.get("exclusion", "").lower() and "prestigieuse" not in call.get("tags", ""):
        return False
    if "mid-career" in call.get("niveau", "").lower():
        return True  # filtrage optionnel
    if call.get("localisation") not in ["France", "Paris", "Île-de-France", "Alsace", "Strasbourg", "Grand Est", "Bretagne", "Bourgogne"]:
        if not call.get("international", False):
            return False
    return True

def format_call(call):
    couleur = {
        "élevée": "🟢",
        "moyenne": "🟡",
        "faible": "🔴"
    }.get(call.get("chance", "moyenne"), "🟡")

    return f"""{couleur} **{call['titre']}**
🗓️ Deadline : {call['deadline']}
📍 Lieu : {call['localisation']}
🔗 Lien : {call['lien']}

📝 Commentaire : {call.get('commentaire', 'Pas de commentaire.')}
"""

def make_id(titre, lien):
    return hashlib.sha256(f"{titre}-{lien}".encode()).hexdigest()
