class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50 

    def get_marque(self):
        return self._marque

    def set_marque(self, marque):
        self._marque = marque

    def get_modele(self):
        return self._modele

    def set_modele(self, modele):
        self._modele = modele

    def get_annee(self):
        return self._annee

    def set_annee(self, annee):
        self._annee = annee

    def get_kilometrage(self):
        return self._kilometrage

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    def est_en_marche(self):
        return self._en_marche

    def demarrer(self):
        if self._verifier_plein() and not self._en_marche:
            self._en_marche = True
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer.")

    def arreter(self):
        if self._en_marche:
            self._en_marche = False
            print("La voiture s'est arrêtée.")
        else:
            print("La voiture est déjà arrêtée.")

    def _verifier_plein(self):
        return self._reservoir > 5

ma_voiture = Voiture("Toyota", "Camry", 2022, 15000)

ma_voiture.demarrer()

ma_voiture._reservoir = 10

ma_voiture.demarrer()

ma_voiture.arreter()

en_marche = ma_voiture.est_en_marche()
print("La voiture est en marche :", en_marche)
