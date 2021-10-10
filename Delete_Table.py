import cx_Oracle

try:
    conn = cx_Oracle.connect('mydatabase/mydatabase@//localhost:1521/xe')
except Exception as err:
    print('Error while connecting',err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        sql = """DELETE FROM STUDENT WHERE STUDENT_NAME='RACHANA'"""
        cur.execute(sql)
    except Exception as err:
        print('Error while updating  the table',err)
    else:
        conn.commit()
        print('Data deleted')
finally:
    cur.close()
    conn.close()
