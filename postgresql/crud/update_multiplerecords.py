import psycopg2

def updateInBulk(records):
    try:
        ps_connection = psycopg2.connect(database="postdb", 
                                      user='postgres', 
                                      password='password', 
                                      host='127.0.0.1', 
                                      port= '5432')

        cursor = ps_connection.cursor()

        # Update multiple records
        sql_update_query = """Update employee set age = %s where income = %s"""
        cursor.executemany(sql_update_query, records)
        ps_connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


tuples = [(24,6000), (25,60010)]
updateInBulk(tuples)
