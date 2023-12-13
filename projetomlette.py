import time

class Personnage:
    def __init__(self, nom, lieu, argent):
        self.nom = nom
        self.lieu = lieu
        self.argent = argent
        self.main_droite = []
        self.main_gauche = []

    def se_deplacer(self, lieu):
        self.lieu = lieu
        print(f"{self.nom} est actuellement à la {self.lieu}")

    def payer_article(self, article):
        self.argent -= article.prix
        print(f"{self.nom} a payé {article.prix} euros pour {article.nom}. Argent restant : {self.argent} euros")

    def couper(self, ingredient, outil):
        if outil.action == 'entier' and ingredient.etats[0] == 'entier':
            outil.action = 'coupé'
            ingredient.etats[0] = 'coupé'
            print(f"{self.nom} a coupé {ingredient.nom} avec un {outil.nom}")

