"""
Auteurs    : Christian Clay et Kevin Tran
Description: Module contenant la classe Artiste.
             Gère les propriétés d'un artiste musical: nom, genre, année de début,
             pays d'origine et liste de chansons.
"""


class Artiste:
    # Représente un artiste musical avec ses informations.

    def __init__(self, str_nom, str_genre, int_annee, str_pays, lst_chansons):
    
        self.str_nom = str_nom
        self.str_genre = str_genre
        self.int_annee = int_annee
        self.str_pays = str_pays
        self.lst_chansons = lst_chansons


    # @properties and @setters
    
    @property
    def str_nom(self):
        return self._str_nom

    @str_nom.setter
    def str_nom(self, str_nom):
        self._str_nom = str_nom


    @property
    def str_genre(self):
        return self._str_genre

    @str_genre.setter
    def str_genre(self, str_genre):
        self._str_genre = str_genre


    @property
    def int_annee(self):
        return self._int_annee

    @int_annee.setter
    def int_annee(self, int_annee):
        if int_annee < 0 or int_annee > 2026:
            # Lève une exception qui sera attrapée par le try/except du programme principal.
            raise ValueError("L'année doit être entre 0 et 2026.")
        self._int_annee = int_annee


    @property
    def str_pays(self):
        return self._str_pays

    @str_pays.setter
    def str_pays(self, str_pays):
        self._str_pays = str_pays

   
    @property
    def lst_chansons(self):
        return self._lst_chansons

    @lst_chansons.setter
    def lst_chansons(self, lst_chansons):
        self._lst_chansons = lst_chansons
