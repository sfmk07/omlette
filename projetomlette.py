import time

# Classe Personnage
class Personnage:
    def __init__(self, nom, lieu, argent):
        self.nom = nom
        self.lieu = lieu
        self.argent = argent
        self.main_droite = []
        self.main_gauche = []

    def se_deplacer(self, lieu):
        self.lieu = lieu.nom
        print(f"{self.nom} est actuellement à la {self.lieu}")

    def payer_article(self, article):
        self.argent -= article.prix
        print(f"Il reste {self.argent} euros à {self.nom}")

    def couper(self, ingredient, outil):
        if outil.nom == "Couteau" and ingredient.etat == "entier":
            ingredient.etat = "coupé"
            print(f"{self.nom} a coupé {ingredient.nom} avec {outil.nom}")

# Classe Lieu
class Maison:
    def __init__(self):
        self.nom = 'maison'
        self.personnes = []

class Epicerie:
    def __init__(self):
        self.nom = 'épicerie'
        self.personnes = []
        self.paniers = [{"type": "panier", "contenu": []}]
        self.ingredients = []

# Classe Outil
class Couteau:
    def __init__(self):
        self.nom = "Couteau"
        self.action = "entier"

# Classe Ingrédient
class Ingredient:
    def __init__(self, nom, prix):
        self.nom = nom
        self.etat = "entier"
        self.prix = prix

# Classe Poele
class Poele:
    def __init__(self):
        self.contenu = []

    def cuire(self):
        time.sleep(4)
        if self.contenu:
            self.contenu[0].etat = 'cuit'
            print("Notre omelette est cuite :)")

# Classe Bol
class Bol:
    def __init__(self):
        self.contenu = []

    def melanger(self, nom_melange):
        new_melange = Ingredient(nom_melange, 0)
        new_melange.etat = 'pas cuit'
        self.contenu = [new_melange]
        print(f"{nom_melange} a été mélangé dans le bol")

# Exemple de déroulement du scénario
maison = Maison()
epicerie = Epicerie()
personnage = Personnage("Sofiane", "quelque part", 100)

# Déplacer le personnage à la maison
personnage.se_deplacer(maison)

# Ajouter des ingrédients à l'épicerie pour l'exemple
epicerie.ingredients.append(Ingredient("Oeuf", 0.5))
epicerie.ingredients.append(Ingredient("Lait", 1))
epicerie.ingredients.append(Ingredient("Farine", 0.75))

# Déplacer le personnage à l'épicerie
personnage.se_deplacer(epicerie)

# Prendre un panier
panier = epicerie.paniers[0]
personnage.main_droite.append(panier)
print(f"{personnage.nom} a pris un panier")

# Acheter des ingrédients
for ingredient in epicerie.ingredients:
    copie_ingredient = Ingredient(ingredient.nom, ingredient.prix)
    panier["contenu"].append(copie_ingredient)
    print(f"{personnage.nom} a pris {copie_ingredient.nom}")
    personnage.payer_article(copie_ingredient)

# Retourner à la maison
personnage.se_deplacer(maison)

# Mettre les ingrédients dans le bol
bol = Bol()
for ingredient in panier["contenu"]:
    bol.contenu.append(ingredient)
    print(f"{ingredient.nom} mis dans le bol")
panier["contenu"].clear()

# Retourner à l'épicerie pour rapporter le panier
personnage.se_deplacer(epicerie)
personnage.main_droite.remove(panier)
epicerie.paniers.append(panier)
print(f"Panier retourné à l'épicerie")

# Retourner à la maison
personnage.se_deplacer(maison)

# Couper les ingrédients si nécessaire
couteau = Couteau()
for ingredient in bol.contenu:
    personnage.couper(ingredient, couteau)

# Mélanger les ingrédients
bol.melanger
