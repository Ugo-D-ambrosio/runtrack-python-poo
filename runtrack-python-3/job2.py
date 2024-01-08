class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self._numero_compte} - Titulaire : {self._prenom} {self._nom}")
        print(f"Solde : {self._solde}€")

    def afficher_solde(self):
        print(f"Solde du compte : {self._solde}€")

    def versement(self, montant):
        if montant > 0:
            self._solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde : {self._solde}€")
        else:
            print("Le montant du versement doit être supérieur à zéro.")

    def retrait(self, montant):
        if self._decouvert or self._solde >= montant:
            self._solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self._solde}€")
        else:
            print("Solde insuffisant ou opération non autorisée.")

    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * (taux_agios / 100)
            self._solde -= agios
            print(f"Agios de {agios}€ appliqués. Nouveau solde : {self._solde}€")

    def virement(self, autre_compte, montant):
        if montant > 0 and self._solde >= montant:
            self._solde -= montant
            autre_compte.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte n°{autre_compte._numero_compte}.")
        else:
            print("Montant invalide ou solde insuffisant pour effectuer le virement.")


compte1 = CompteBancaire(1, "Doe", "John", 1000, True)
compte1.afficher()
compte1.afficher_solde()

compte1.versement(500)
compte1.retrait(1500)

compte1.agios(2)

compte2 = CompteBancaire(2, "Smith", "Alice", -500, True)
compte2.afficher()
compte2.afficher_solde()

compte1.virement(compte2, 1000)
compte1.afficher()
compte2.afficher()
