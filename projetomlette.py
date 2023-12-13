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

class Lieu:
    def __init__(self, nom):
        self.nom = nom
        self.personnes = []

class Outil:
    def __init__(self, nom):
        self.nom = nom
        self.action = 'entier'

class Ingredient:
    def __init__(self, nom, etats, prix):
        self.nom = nom
        self.etats = etats
        self.prix = prix

class Epicerie(Lieu):
    def __init__(self, nom, ingrédients):
        super().__init__(nom)
        self.paniers = [{'type': 'panier', 'contenu': []}]
        self.ingrédients = ingrédients

class Poele:
    def __init__(self):
        self.contenu = []

    def cuire(self):
        time.sleep(4)
        self.contenu[0].etats[0] = 'cuit'
        print("L'omelette est cuite :)")

class Bol:
    def __init__(self):
        self.contenu = []

    def melanger(self, nom_melange):
        new_melange = Ingredient(nom_melange, ['pas cuit'], 0)
        self.contenu = [new_melange]
        print(f"{nom_melange} a été mélangé dans le bol.")

# Début du scénario
# Création des ingrédients
oeuf = Ingredient('œuf', ['entier'], 1.0)
lait = Ingredient('lait', ['entier'], 0.5)
sel = Ingredient('sel', ['entier'], 0.2)
poivre = Ingredient('poivre', ['entier'], 0.3)

# Création des lieux
maison = Lieu('maison')
epicerie = Epicerie('épicerie', [oeuf, lait, sel, poivre])

# Création des outils
couteau = Outil('couteau')

# Création des objets de préparation
poele = Poele()
bol = Bol()

# Création du personnage
personnage = Personnage('Sofiane', 'maison', 10.0)

# Indiquer que le personnage est à la maison
personnage.se_deplacer(maison.nom)

# Aller à l'épicerie acheter les ingrédients
personnage.se_deplacer(epicerie.nom)
personnage.main_droite.append(epicerie.paniers[0])
print(f"{personnage.nom} a pris un panier")

# Boucle pour prendre chaque ingrédient dans l'épicerie
for ingredient in epicerie.ingrédients:
    copie_ingredient = Ingredient(ingredient.nom, ingredient.etats, ingredient.prix)
    personnage.main_droite[0]['contenu'].append(copie_ingredient)
    print(f"{personnage.nom} a pris {ingredient.nom}")
    personnage.payer_article(ingredient)

# Retourner à la maison
personnage.se_deplacer(maison.nom)
print(f"{personnage.nom} est de retour à la maison")

# Mettre chaque ingrédient dans le bol
for ingredient in personnage.main_droite[0]['contenu']:
    bol.contenu.append(ingredient)
    print(f"{ingredient.nom} a été mis dans le bol")

# Retourner à l'épicerie pour rapporter le panier
personnage.se_deplacer(epicerie.nom)
epicerie.paniers.append(personnage.main_droite.pop())
print(f"{personnage.nom} a rapporté le panier à l'épicerie")

# Retourner à la maison pour continuer l'omelette
personnage.se_deplacer(maison.nom)
print(f"{personnage.nom} est de retour à la maison")

# Vérifier chaque ingrédient dans le bol et le couper seulement s'il est entier
for ingredient in bol.contenu:
    personnage.couper(ingredient, couteau)

# Mélanger le contenu du bol pour créer une 'omelette'
bol.melanger('omelette')

# Vider le contenu du bol dans la poêle
poele.contenu = bol.contenu
bol.contenu = []
print(f"{personnage.nom} a versé le contenu du bol dans la poêle")

# Cuire l'omelette
poele.cuire()

# Afficher un message final
print("Notre omelette est cuite :)")
