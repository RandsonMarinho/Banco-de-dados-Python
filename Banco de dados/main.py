#    Conexão com banco de dados

import psycopg2 as connector
from Script1 import People

# Abertura de conexão

conection = connector.connect(database = "recuper.db",
                              host = "localhost",
                              user = "postgres",
                              port = "")

cursor = conection.cursor()





#Efetivação do comando
conection.commit()

#Fechando as conexões






