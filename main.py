from datetime import date

from models.Utilisateur import Utilisateur
from services.UtilisateurService import UtilisateurService

if __name__ == '__main__':
    utilisateur = Utilisateur(
        'JO-DPH55',
        'JOSEPH',
        'Daphnée',
        'F',
        date(1999, 11, 18),
        '47440348',
        123456789,
        'josephdaphnee99',
        'novembre18',
        75000.00,
        'A')
    
    utilisateurService = UtilisateurService()
    
    utilisateurService.ajouterUtilisateur(utilisateur)
