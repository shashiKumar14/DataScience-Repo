import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="postgres",
    port= '5432')

cur = conn.cursor()
cur.execute('CREATE TABLE student(id SERIAL PRIMARY KEY,name VARCHAR);')

cur.execute("insert into  student(name) values ('shiva')")
conn.commit()
cur.close()
conn.close()

====================================================================================================================================================
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="suppliers", user='postgres', password='postgres', host='localhost', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

#Preparing query to create a database
# sql = 'CREATE database mydb'

# #Creating a database
# cursor.execute(sql)
# print("Database created successfully........")

# #Fetching all the rows before the update
# print("Contents of the student table: ")
# sql = '''SELECT * from student'''
# cursor.execute(sql)
# print(cursor.fetchall())

# #Updating the records
# sql = "UPDATE student SET name = 'eeshwar' WHERE name = 'shashi'"
# cursor.execute(sql)
# print("Table updated...... ")

# #Fetching all the rows after the update
# print("Contents of the student table after the update operation: ")
# sql = 'SELECT * from student'
# cursor.execute(sql)
# print(cursor.fetchall())

# #Commit your changes in the database
# conn.commit()

# #Closing the connection
# conn.close()


=======================================================================================================================================================



