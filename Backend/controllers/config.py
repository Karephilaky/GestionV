DB_HOST = "bmtsvu1rsfofd0lnkm2s-postgresql.services.clever-cloud.com"
DB_NAME = "bmtsvu1rsfofd0lnkm2s"
DB_USER = "u5ezalrqslbb6bmhtmyj"
DB_PASSWORD = "TIhRNURi5r8wYK8CPFT0dupplDmbuC"
DB_PORT = "50013"

import psycopg2

def config():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
