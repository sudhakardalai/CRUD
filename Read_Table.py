import cx_Oracle

try:
    conn = cx_Oracle.connect('mydatabase/mydatabase@//localhost:1521/xe')
except Exception as err:
    print('Error while connecting',err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        sql = """SELECT * FROM STUDENT"""
        cur.execute(sql)
        row = cur.fetchall()
        print(row)
        # row = cur.fetchone()
        # row2=cur.fetchone()
        # print(row2)

        for index,record in enumerate(row):
            print('Index is ',index,':',record)
    except Exception as err:
        print('Error while fetching  the data',err)
    else:
        print('Completed')
finally:
    cur.close()
    conn.close()
