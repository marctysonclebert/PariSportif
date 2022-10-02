from database.Database import Database
from models.Utilisateur import Utilisateur


class UtilisateurService:
    
    def __init__(self):
        self.__database: Database = Database()
        self.__connection = self.__database.get_connection()
    
    def ajouterUtilisateur(self, utilisateur: Utilisateur):
        sql = "INSERT INTO utilisateurs VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        arguments = (
            utilisateur.get_code(),
            utilisateur.get_nom(),
            utilisateur.get_prenom(),
            utilisateur.get_sexe(),
            utilisateur.get_date_naissance(),
            utilisateur.get_telephone(),
            utilisateur.get_nif_cin(),
            utilisateur.get_nom_utilisateur(),
            utilisateur.get_mot_de_passe(),
            utilisateur.get_solde(),
            utilisateur.get_etat(),
        )
        cursor = self.__connection.cursor()
        cursor.execute(sql, arguments)
        self.__connection.commit()
