import psycopg2

def updateTable(first_name, age):
    try:
        connection = psycopg2.connect(database="postdb", 
                                      user='postgres', 
                                      password='password', 
                                      host='127.0.0.1', 
                                      port= '5432')

        cursor = connection.cursor()

        # print("Table Before updating record ")
        # sql_select_query = """select * from employee where first_name = %s"""
        # cursor.execute(sql_select_query, (first_name,))
        # record = cursor.fetchone()
        # print(record)

        # Update single record now
        sql_update_query = """Update employee set age = %s where first_name = %s"""
        cursor.execute(sql_update_query, (age, first_name))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        # print("Table After updating record ")
        # sql_select_query = """select * from employee where first_name = %s"""
        # cursor.execute(sql_select_query, (first_name,))
        # record = cursor.fetchone()
        # print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

age = 3
first_name = 'Vinay2'
updateTable( first_name,age)
