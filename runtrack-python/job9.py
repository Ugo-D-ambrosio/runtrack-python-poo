class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        prixTTC = self.prixHT + (self.prixHT * self.TVA / 100)
        return prixTTC

    def afficher(self):
        infos = f"Nom du produit : {self.nom}\n"
        infos += f"Prix HT : {self.prixHT} €\n"
        infos += f"TVA : {self.TVA}%"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 15)

print(produit1.afficher())
print(produit2.afficher())

produit1.modifierNom("Laptop")
produit1.modifierPrixHT(900)

print("Nouvelles informations du produit 1 :")
print(produit1.afficher())

prixTTC_produit1 = produit1.calculerPrixTTC()
prixTTC_produit2 = produit2.calculerPrixTTC()

prixTTC_produit1, prixTTC_produit2
