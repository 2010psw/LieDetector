import pymysql
from DB import dbinfo

host=dbinfo.host
user=dbinfo.user
password=dbinfo.password
db=dbinfo.db
charset=dbinfo.charset

def conn():
    conn = pymysql.connect(host=host,
                        user=user,
                        password=password,
                        db=db,
                        charset=charset)
    return conn

def select ():
    con = conn()
    try:
        with con.cursor() as cursor:
            sql = "select * from student"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
    finally:
        con.close()



