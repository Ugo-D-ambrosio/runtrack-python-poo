class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_de_pages = nombre_de_pages
        self._disponible = True 

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

    def vérification(self):
        return self._disponible

    def emprunter(self):
        if self.vérification():
            self._disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour emprunt.")

    def rendre(self):
        if not self.vérification():
            self._disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre est déjà disponible.")

mon_livre = Livre("Titre du livre", "Auteur du livre", 200)

disponible = mon_livre.vérification()
print("Le livre est disponible :", disponible)

mon_livre.emprunter()

disponible_apres_emprunt = mon_livre.vérification()
print("Le livre est disponible après emprunt :", disponible_apres_emprunt)

mon_livre.rendre()

disponible_apres_rendu = mon_livre.vérification()
print("Le livre est disponible après rendu :", disponible_apres_rendu)
