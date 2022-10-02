from mysql.connector import connect


class Database:
    def __init__(self):
        self.__host = 'localhost'
        self.__user = 'codewithmarc'
        self.__password = 'Pass@123'
        self.__database_name = 'pari_sportif'
    
    def get_connection(self):
        return connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database_name)
