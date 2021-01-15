"""ABC
"""
import requests
from bs4 import BeautifulSoup
from classes.quote import Quote
from classes.filemanager import Filemanager
from classes.author import Author
from firebase import firebase



class Sitescrapper:
    """
    get_quotes: return quote list
    ButtonNextExists: next page if next button exists
    """

    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url).content, 'lxml')
        self.quote_lst = []

                # Delete BDD
        self.firebase = firebase.FirebaseApplication('https://pythoncnam-default-rtdb.europe-west1.firebasedatabase.app/', None)
        self.firebase.delete('pythoncnam/', 'tuto')

    def get_quotes(self):
        """
        Return : quote_lst(Array of Quotes) for all quotes in the page
        """
        quote_lst = []
        quotes = self.soup.find_all('div')
        for quote in quotes:
            if 'class' in quote.attrs and 'quote' in quote['class']:
                quote_lst.append(Quote(quote))
        return quote_lst

    def button_next_exists(self):
        """
        Search if next button exists
        Return : next_btn(exists(boolean),url(string))
        """

        next_btn = self.soup.find_all("li", {"class": "next"})
        print(next_btn)
        return (len(next_btn) > 0,
                'http://quotes.toscrape.com'+next_btn[0].a.get('href')
                if len(next_btn) > 0 else '')

    def parse_pages(self):
        """
        Browse the page while button_next_exists is true
        """

        while True:
            self.quote_lst += self.get_quotes()
            btn_next = self.button_next_exists()
            if btn_next[0]:
                self.url = btn_next[1]
                self.soup = BeautifulSoup(
                                requests.get(btn_next[1]).content,
                                'lxml')
            else:
                break
        self.print_files()


               
        
    def print_files(self):
        """
        prints an xlsx file a txt file and a md file in the Result folder
        """

        file_manager = Filemanager(self.quote_lst)
        file_manager.edit_md_file()
        file_manager.edit_xlsx_file()
        file_manager.edit_txt_file()
