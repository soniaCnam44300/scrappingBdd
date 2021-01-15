"""ABC
"""
from classes.sitescrapper import Sitescrapper



site_scrapper = Sitescrapper('http://quotes.toscrape.com/')
site_scrapper.parse_pages()

# site_scrapper.bddInsert()

# print(get_list_games())




