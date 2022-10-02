from datetime import date


class Utilisateur:
    def __init__(self,
                 code: str,
                 nom: str,
                 prenom: str,
                 sexe: str,
                 date_naissance: date,
                 telephone: str,
                 nif_cin: int,
                 nom_utilisateur: str,
                 mot_de_passe: str,
                 solde: float,
                 etat: str):
        self.__code = code
        self.__nom = nom
        self.__prenom = prenom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__date_naissance = date_naissance
        self.__telephone = telephone
        self.__nif_cin = nif_cin
        self.__nom_utilisateur = nom_utilisateur
        self.__mot_de_passe = mot_de_passe
        self.__solde = solde
        self.__etat = etat
    
    # GETTERS
    def get_code(self):
        return self.__code
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_sexe(self):
        return self.__sexe
    
    def get_date_naissance(self):
        return self.__date_naissance
    
    def get_telephone(self):
        return self.__telephone
    
    def get_nif_cin(self):
        return self.__nif_cin
    
    def get_nom_utilisateur(self):
        return self.__nom_utilisateur
    
    def get_mot_de_passe(self):
        return self.__mot_de_passe
    
    def get_solde(self):
        return self.__solde
    
    def get_etat(self):
        return self.__etat
    
    # SETTERS
    def set_code(self, code: str):
        self.__code = code
    
    def set_nom(self, nom: str):
        self.__nom = nom
    
    def set_prenom(self, prenom: str):
        self.__prenom = prenom
    
    def set_sexe(self, sexe: str):
        self.__sexe = sexe
    
    def set_date_naissance(self, date_naissance: date):
        self.__date_naissance = date_naissance
    
    def set_telephone(self, telephone: str):
        self.__telephone = telephone
    
    def set_nif_cin(self, nif_cin: str):
        self.__nif_cin = nif_cin
    
    def set_nom_utilisateur(self, nom_utilisateur: str):
        self.__nom_utilisateur = nom_utilisateur
    
    def set_mot_de_passe(self, mot_de_passe: str):
        self.__mot_de_passe = mot_de_passe
    
    def set_solde(self, solde: str):
        self.__solde = solde
    
    def set_etat(self, etat: str):
        self.__etat = etat
    
    def to_string(self):
        return f"Code: {self.get_code()}" \
               f"\nNom: {self.get_nom()}" \
               f"\nPrenom: {self.get_prenom()}" \
               f"\nSexe: {self.get_sexe()}" \
               f"\nDate De Naissance: {self.get_date_naissance()}" \
               f"\nTéléphone: {self.get_telephone()}" \
               f"\nNif/Cin: {self.get_nif_cin()}" \
               f"\nNom D'Utilisateur: {self.get_nom_utilisateur()}" \
               f"\nMot De Passe: {self.get_mot_de_passe()}" \
               f"\nSolde: {self.get_solde()}" \
               f"\nÉtat: {self.get_etat()}"
