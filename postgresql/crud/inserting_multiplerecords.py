import psycopg2

def bulkInsert(records):
    try:
        connection = psycopg2.connect(database="postdb", 
                                      user='postgres', 
                                      password='password', 
                                      host='127.0.0.1', 
                                      port= '5432')
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO employee (first_name,last_name,age,sex,income) 
                           VALUES (%s,%s,%s,%s,%s) """

        # executemany() to insert multiple rows
        cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

records_to_insert = [('Vinay1', 'Battacharya1', 201, 'M', 6000),('Vinay11', 'Battacharya11', 2011, 'M', 60010)]
#works [['Vinay2', 'Battacharya2', 2012, 'M', 60002]]
bulkInsert(records_to_insert)