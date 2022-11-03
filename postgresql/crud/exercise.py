import psycopg2
import pandas as pd
try:
    connection = psycopg2.connect(database="postdb", 
                                user='postgres', 
                                password='password', 
                                host='127.0.0.1', 
                                port= '5432')
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from employee"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()
    print("mobile_records======>",mobile_records)#list of tuple records
    df = pd.DataFrame(mobile_records, columns =['first_name', 'last_name','Age', 'sex','income'])
  
    print(df) 
    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
