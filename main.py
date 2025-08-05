import os
from dotenv import load_dotenv
from scraper_manager import collect_all_opencalls
from filter_and_format import filter_and_format_opencalls
from mailer import send_email
from utils import load_previously_sent_ids, save_sent_ids

load_dotenv()

def main():
    all_calls = collect_all_opencalls()
    previous_ids = load_previously_sent_ids()

    nouveaux, rappels = filter_and_format_opencalls(all_calls, previous_ids)

    if nouveaux or rappels:
        send_email(nouveaux, rappels)
        save_sent_ids([call['id'] for call in nouveaux + rappels])
    else:
        print("Aucun nouvel appel valide trouvé.")
        # Optionnel : pour tester que l’envoi fonctionne même sans appel détecté
        send_email([], [])  # à supprimer plus tard si tout fonctionne

if __name__ == "__main__":
    main()
