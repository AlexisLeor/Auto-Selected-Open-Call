from scrapers.cnap import scrape_cnap
from scrapers.cipac import scrape_cipac
# from scrapers.autres import scrape_autres # Ajouter les autres scrapers ici

def collect_all_opencalls():
    all_calls = []
    all_calls += scrape_cnap()
    all_calls += scrape_cipac()
    # all_calls += scrape_autres()
    return all_calls
