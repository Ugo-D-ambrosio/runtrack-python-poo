import random

# Classe Carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

# Classe Jeu
class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def donner_carte(self):
        if len(self.paquet) > 0:
            return self.paquet.pop()
        else:
            return None

if __name__ == "__main__":
    jeu = Jeu()
    jeu.melanger()
    
    main_joueur = [jeu.donner_carte(), jeu.donner_carte()]
    main_croupier = [jeu.donner_carte(), jeu.donner_carte()]
    
    print("Main du joueur:")
    for carte in main_joueur:
        print(carte)
    
    print("\nMain du croupier:")
    print(main_croupier[0]) 
