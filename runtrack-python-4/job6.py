class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("La voiture démarre. Prêt à rouler !")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("La moto démarre. En route !")

ma_voiture = Voiture("Toyota", "Corolla", 2022, 25000)
print("Informations de la voiture:")
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

ma_moto = Moto("Honda", "CBR500R", 2021, 7000)
print("\nInformations de la moto:")
ma_moto.informationsVehicule()
ma_moto.demarrer()
