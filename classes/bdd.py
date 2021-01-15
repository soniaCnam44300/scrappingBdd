"""Classe bdd
"""
from firebase import firebase
from classes.sitescrapper import Sitescrapper
from classes.author import Author

class Bdd:
    """
    fsqfsdq
    """ 
    def __init__(self, URL):
        self.URL = URL
        firebase = firebase.FirebaseApplication(URL, None)
        data =  {'Name': 'John Doe',
                'RollNo': 3,
                'Percentage': 70.02
                }
        result = firebase.post('pythoncnam/tuto',data)
        print(result)