from cipac import scrape_cipac
from cnap import scrape_cnap
from ceaac import scrape_ceaac
from villa_kujoyama import scrape_kujoyama
from villa_medicis import scrape_medicis
from institut_francais import scrape_institut_francais
from goethe_institut import scrape_goethe
from transartists import scrape_transartists
from pro_helvetia import scrape_pro_helvetia
from villa_albertine import scrape_albertine
from villa_ndar import scrape_villa_ndar
from villa_swagatam import scrape_villa_swagatam

def collect_all_opencalls():
    all_calls = []
    for scrape_func in [
        scrape_cipac,
        scrape_cnap,
        scrape_ceaac,
        scrape_kujoyama,
        scrape_medicis,
        scrape_institut_francais,
        scrape_goethe,
        scrape_transartists,
        scrape_pro_helvetia,
        scrape_albertine,
        scrape_villa_ndar,
        scrape_villa_swagatam,
    ]:
        try:
            calls = scrape_func()
            all_calls.extend(calls)
        except Exception as e:
            print(f"Erreur lors du scraping de {scrape_func.__name__}: {e}")
    return all_calls
