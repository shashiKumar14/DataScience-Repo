import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postdb", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   income FLOAT
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()


#ref: https://pynative.com/python-postgresql-select-data-from-table/