from autoscraper import AutoScraper


tbilisi_city_id = 95
usd_currency_id = 2


url = f"https://home.ss.ge/en/real-estate/l/Flat/For-Rent?cityIdList={tbilisi_city_id}&currencyId={usd_currency_id}"

wanted_list = ["1 room Flat For Rent. Didube ", "1,000 ₾", "https://home.ss.ge/en/real-estate/3-room-Flat-For-Rent-Chugureti-29770140", "38 m²"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)

print(result)
similar = scraper.get_result_similar(url, grouped=True)
print(similar)

scraper.set_rule_aliases({"rule_ku5x": "title", "rule_6y8o": "price", "rule_bskw": "squares"})
scraper.keep_rules(["rule_ku5x", "rule_6y8o", "rule_bskw"])

scraper.get_result_exact("https://home.ss.ge/en/real-estate/l/Flat/For-Rent?cityIdList=95&currencyId=2&page=2")

scraper.save("flat-search")

