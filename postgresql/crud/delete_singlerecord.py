import psycopg2


def deleteData(first_name):
    try:
        connection = psycopg2.connect(database="postdb", 
                                      user='postgres', 
                                      password='password', 
                                      host='127.0.0.1', 
                                      port= '5432')

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from employee where first_name = %s"""
        cursor.execute(sql_delete_query, (first_name,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

first_name = 'Vinay2'
deleteData(first_name)
