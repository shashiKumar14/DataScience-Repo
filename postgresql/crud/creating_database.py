import psycopg2

conn = psycopg2.connect( user = "postgres", password = "password", 
                           host = "127.0.0.1", port = "5432")
print(conn)
conn.autocommit = True
cur = conn.cursor()

query='''CREATE DATABASE postdb''';
cur.execute(query)

conn.close()

