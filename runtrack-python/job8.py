import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        return f"Rayon du cercle : {self.rayon}"

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

infos_cercle1 = cercle1.afficherInfos()
circonference_cercle1 = cercle1.circonference()
diametre_cercle1 = cercle1.diametre()
aire_cercle1 = cercle1.aire()

infos_cercle2 = cercle2.afficherInfos()
circonference_cercle2 = cercle2.circonference()
diametre_cercle2 = cercle2.diametre()
aire_cercle2 = cercle2.aire()

infos_cercle1, circonference_cercle1, diametre_cercle1, aire_cercle1, infos_cercle2, circonference_cercle2, diametre_cercle2, aire_cercle2
