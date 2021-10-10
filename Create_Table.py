import cx_Oracle

try:
    conn = cx_Oracle.connect('mydatabase/mydatabase@//localhost:1521/xe')
except Exception as err:
    print('Error while connecting',err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        sql_create = """CREATE TABLE STUDENT(STUDENT_NO NUMBER(3),STUDENT_NAME VARCHAR2(30),DOB DATE,DOJ DATE)"""
        cur.execute(sql_create)
    except Exception as err:
        print('Error while creating table',err)
    else:
        print('Table created')
        conn.commit()
finally:
    cur.close()
    conn.close()
