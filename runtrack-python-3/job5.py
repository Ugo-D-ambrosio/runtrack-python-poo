import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        degats = random.randint(10, 20) 
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

class Jeu:
    def __init__(self):
        self.niveau = 1 

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancer_jeu(self):
        self.choisir_niveau()

        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 80
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 100
        elif self.niveau == 3:
            vie_joueur = 70
            vie_ennemi = 120
        else:
            print("Niveau invalide. Choisissez un niveau parmi 1, 2 ou 3.")
            return

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            print(f"{joueur.nom} - Points de vie : {joueur.vie}")
            print(f"{ennemi.nom} - Points de vie : {ennemi.vie}")
            print("-------------------------")
            joueur.attaquer(ennemi)
            if ennemi.vie > 0:
                ennemi.attaquer(joueur)

        if joueur.vie > 0:
            print(f"{joueur.nom} a gagné !")
        else:
            print(f"{ennemi.nom} a gagné !")

jeu = Jeu()
jeu.lancer_jeu()
