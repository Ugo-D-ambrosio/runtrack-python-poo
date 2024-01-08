class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut = "en cours" 

    def ajouter_plat(self, nom_plat, prix_plat):
        if self._statut == "en cours":
            if nom_plat in self._plats_commandes:
                self._plats_commandes[nom_plat]['quantite'] += 1
            else:
                self._plats_commandes[nom_plat] = {'prix': prix_plat, 'quantite': 1}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print("La commande est déjà terminée ou annulée, impossible d'ajouter un plat.")

    def annuler_commande(self):
        if self._statut == "en cours":
            self._statut = "annulée"
            self._plats_commandes.clear()
            print("La commande a été annulée.")
        else:
            print("La commande est déjà terminée ou annulée.")

    def _calculer_total(self):
        total = sum(plat_info['prix'] * plat_info['quantite'] for plat_info in self._plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande n°{self._numero_commande} - Statut : {self._statut}")
        for nom_plat, plat_info in self._plats_commandes.items():
            prix_unitaire = plat_info['prix']
            quantite = plat_info['quantite']
            total_plat = prix_unitaire * quantite
            print(f"- {nom_plat}: {quantite} x {prix_unitaire}€ = {total_plat}€")
        total_commande = self._calculer_total()
        print(f"Total à payer : {total_commande}€")

    def calculer_tva(self, taux_tva):
        total_commande = self._calculer_total()
        tva = total_commande * (taux_tva / 100)
        return tva

commande1 = Commande(1)
commande1.ajouter_plat("Pizza", 12.99)
commande1.ajouter_plat("Burger", 8.99)
commande1.afficher_commande()

commande1.calculer_tva(10)

commande1.annuler_commande()
commande1.afficher_commande()
