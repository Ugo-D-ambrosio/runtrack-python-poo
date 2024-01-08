class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def set_longueur(self, longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, largeur):
        self._largeur = largeur

mon_rectangle = Rectangle(10, 5)

print("Longueur initiale :", mon_rectangle.get_longueur())
print("Largeur initiale :", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(7)

print("Nouvelle longueur :", mon_rectangle.get_longueur())
print("Nouvelle largeur :", mon_rectangle.get_largeur())
