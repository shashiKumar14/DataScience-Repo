import psycopg2


def deleteInBulk(records):
    try:
        ps_connection = psycopg2.connect(database="postdb", 
                                      user='postgres', 
                                      password='password', 
                                      host='127.0.0.1', 
                                      port= '5432')
        cursor = ps_connection.cursor()
        ps_delete_query = """Delete from employee where income = %s"""
        cursor.executemany(ps_delete_query, records)
        ps_connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Record Deleted")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")

# list of tuples contains database IDs
tuples = [(60010,), (6000,)]
deleteInBulk(tuples)
