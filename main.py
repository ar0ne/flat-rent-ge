
from autoscraper import AutoScraper
from flask import Flask

app = Flask(__name__)


tbilisi_city_id = 95
usd_currency_id = 2

SEARCH_URL = f"https://home.ss.ge/en/real-estate/l/Flat/For-Rent?cityIdList={tbilisi_city_id}&currencyId={usd_currency_id}"


home_ge_scraper = AutoScraper()
home_ge_scraper.load("flat-search")

def get_flats_from_home_ge(page: int = 1) -> list[dict]:
    url = f"{SEARCH_URL}&{page=}"
    result: dict[str, str] = home_ge_scraper.get_result_similar(url, group_by_alias=True)
    # prices contain GEL and USD

    return aggregate_results(result)

def aggregate_results(result: dict) -> list[dict]:
    final_result = []
    for i in range(len(list(result.values())[0])):
        final_result.append({alias: result[alias][i] for alias in result})
    return final_result

def find_flats(page_num: int = 3) -> list[dict]:
    
    result = []
    for page in range(page_num):
        page_result = get_flats_from_home_ge(page)
        result.extend(page_result)
    return result

@app.route("/")
def main():
    return find_flats()
