"""ABC
"""


class Author:
    """
    Attributes:
    name(string): Nom de l'auteur
    birthdate(string): Date de naissance de l'auteur
    description(string): Courte biographie de l'auteur
    """

    def __init__(self, soupAuteur):
        divs = soupAuteur.find_all("div",
                                   {"class": "author-details"})
        div = divs[0]
        self.name = div.find_all("h3",
                                 {"class": "author-title"})[0]\
                       .string\
                       .replace('\n', '')
        self.birthdate = div.find_all("span",
                                      {"class": "author-born-date"})[0]\
                            .string\
                            .replace('\n', '')
        self.description = div.find_all("div",
                                        {"class": "author-description"})[0]\
                              .string\
                              .replace('\n', '')



        
    
