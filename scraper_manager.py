from scrapers.cnap import scrape_cnap
from scrapers.cipac import scrape_cipac
from scrapers.villa_kujoyama import scrape_villa_kujoyama
from scrapers.villa_medicis import scrape_villa_medicis
from scrapers.villa_albertine import scrape_villa_albertine
from scrapers.pro_helvetia import scrape_pro_helvetia
from scrapers.transartists import scrape_transartists
from scrapers.ceaac import scrape_ceaac
from scrapers.goethe_institut import scrape_goethe_institut
from scrapers.institut_francais import scrape_institut_francais
from scrapers.villa_velazquez import scrape_villa_velazquez
from scrapers.villa_swagatam import scrape_villa_swagatam
from scrapers.villa_ndar import scrape_villa_ndar

def run_all_scrapers():
    all_calls = []
    all_calls.extend(scrape_cnap())
    all_calls.extend(scrape_cipac())
    all_calls.extend(scrape_villa_kujoyama())
    all_calls.extend(scrape_villa_medicis())
    all_calls.extend(scrape_villa_albertine())
    all_calls.extend(scrape_pro_helvetia())
    all_calls.extend(scrape_transartists())
    all_calls.extend(scrape_ceaac())
    all_calls.extend(scrape_goethe_institut())
    all_calls.extend(scrape_institut_francais())
    all_calls.extend(scrape_villa_velazquez())
    all_calls.extend(scrape_villa_swagatam())
    all_calls.extend(scrape_villa_ndar())
    return all_calls
