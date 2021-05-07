import psycopg2

class Connection_icfes:

    def __init__(self):
        self.connection = None

    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5432",dbname="icfes",user="postgres",password="Gabriela1")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()
