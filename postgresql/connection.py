# import packages
import psycopg2
import pandas as pd

# establish connections
import psycopg2.extras as extras


conn1 = psycopg2.connect(
	database="data",
    user='postgres',
    password='empower',
    host='127.0.0.1',
    port= '5432'
)

# conn1.autocommit = True
cursor = conn1.cursor()

sql = '''CREATE TABLE if not exists airlines_final1(id int ,day
char(20) ,airline char(20),destination char(20));'''
  
# creating a cursor
cursor = conn1.cursor()
cursor.execute(sql)
data = pd.read_csv("airlines_final.csv")
  
data = data[["id", "day", "airline", "destination"]]
def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
    print("tuples===>",tuples)
  
    cols = ','.join(list(df.columns))
    print("cols======>",cols)

  
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn1.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn1.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn1.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()
# using the function defined
execute_values(conn1, data, 'airlines_final1')
conn1.close()