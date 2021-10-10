import cx_Oracle

try:
    conn = cx_Oracle.connect('mydatabase/mydatabase@//localhost:1521/xe')
except Exception as err:
    print('Error while connecting',err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        sql_insert = """INSERT INTO STUDENT VALUES(:1,:2,:3,:4)"""
        student_info = [(101,'Ashutosh Pradhan','10-May-1998','15-Jul-2000'),(102,'Sudhakar Dalai','19-Aug-1997','10-Jul-2000'),(103,'Ram','22-Oct-1996','25-Jul-1999'),(104,'Rachana','14-Feb-1999','10-Mar-2001')]
        cur.executemany(sql_insert,student_info)
    except Exception as err:
        print('Error while inserting data',err)
    else:
        print('Insert Completed')
        conn.commit()
finally:
    cur.close()
    conn.close()
