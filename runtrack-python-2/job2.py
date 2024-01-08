class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nombre_de_pages(self):
        return self._nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self._nombre_de_pages = nombre_de_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")

mon_livre = Livre("Titre du livre", "Auteur du livre", 200)

print("Titre du livre :", mon_livre.get_titre())
print("Auteur du livre :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nombre_de_pages())

mon_livre.set_titre("Nouveau titre")
mon_livre.set_auteur("Nouvel auteur")
mon_livre.set_nombre_de_pages(300)

print("Nouveau titre :", mon_livre.get_titre())
print("Nouvel auteur :", mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_nombre_de_pages())

mon_livre.set_nombre_de_pages(-100)
