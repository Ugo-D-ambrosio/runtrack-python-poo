class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

mon_rectangle = Rectangle(5, 3)

aire_rectangle = mon_rectangle.aire()

print(f"L'aire du rectangle est : {aire_rectangle}")
