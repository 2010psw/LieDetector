import pymysql
from DB import dbinfo


host=dbinfo.host
user=dbinfo.user
password=dbinfo.password
db=dbinfo.db
charset=dbinfo.charset

################연결객체정보################################
def conn():
    conn = pymysql.connect(host=host,
                        user=user,
                        password=password,
                        db=db,
                        charset=charset)
    return conn
################################################################


##############id검색################################
def select_id():
    con = conn()
    try:
        with con.cursor() as cursor:
            sql = "select * from id"
            cursor.execute(sql)
            result = cursor.fetchall()
            a = list(result)
            return_str = []
            for i in a:
                str = list(i)
                return_str.append(str[0])
    finally:
        con.close()
        return return_str
######################################################
# 테스트코드
# test = select_id()
# print('select_id() 정보')
# print(type(test))
# print(test)



#########################gsr 검색#########################
def select_gsr(id):
    con = conn()

    try:
        with con.cursor() as cursor:
            # sql = "select gsr0, gsr1, gsr2, gsr3, gsr4, gsr5, gsr6, gsr7, gsr8, gsr9 from gsr where gid = %s;"
            sql = "select gsr0, gsr1, gsr2, gsr3, gsr4, gsr5, gsr6, gsr7, gsr8, gsr9 from gsr where gid = %s"
            cursor.execute(sql, (id))
            result = cursor.fetchall()
            list = []
            for i in result[0]:
                list.append(i)

    except Exception as msg:
        print(msg)
    finally:
        con.close()
        return list
################################################################
# 테스트코드
# id = 'aaaa'
# list = select_gsr(id)
# print(list)


#########################hrt 검색#########################
def select_hrt(id):
    con = conn()

    try:
        with con.cursor() as cursor:
            sql = "select hrt0, hrt1, hrt2, hrt3, hrt4, hrt5, hrt6, hrt7, hrt8, hrt9 from hrt where hid = %s"
            cursor.execute(sql, (id))
            result = cursor.fetchall()
            list = []
            for i in result[0]:
                list.append(i)

    except Exception as msg:
        print(msg)
    finally:
        con.close()
        return list
################################################################
#########################id 검색#########################
def select_lb(id):
    con = conn()
    a = -1
    try:
        with con.cursor() as cursor:
            sql = "select lb from lb where lid = %s"
            cursor.execute(sql, (id))
            result = cursor.fetchall()
            for i in result[0]:
                a = i

    except Exception as msg:
        print(msg)
    finally:
        con.close()
        return a
################################################################

###########id 입력##############
def ins_id(str_id):
    con = conn()
    try:
        cursor = con.cursor()

        sql = """INSERT INTO id (id) VALUES (%s)"""
        cursor.execute(sql, (str_id))
        con.commit()
    except Exception as msg:
        print(msg)
    finally:
        con.close()
################################

################gsr 입력################
def ins_gsr(id, gsr_list):
    con = conn()
    try:
        cursor = con.cursor()

        sql = """INSERT INTO gsr (gid, gsr0, gsr1, gsr2, gsr3, gsr4, gsr5, gsr6, gsr7, gsr8, gsr9) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (id, gsr_list[0], gsr_list[1], gsr_list[2],gsr_list[3],gsr_list[4],gsr_list[5],
                             gsr_list[6],gsr_list[7],gsr_list[8],gsr_list[9]))
        con.commit()
    except Exception as msg:
        print(msg)
    finally:
        con.close()
################################################

################hrt 입력################################
def ins_hrt(id, hrt_list):
    con = conn()
    try:
        cursor = con.cursor()

        sql = """INSERT INTO hrt (hid, hrt0, hrt1, hrt2, hrt3, hrt4, hrt5, hrt6, hrt7, hrt8, hrt9) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (id, hrt_list[0], hrt_list[1], hrt_list[2],hrt_list[3],hrt_list[4],hrt_list[5],
                             hrt_list[6],hrt_list[7],hrt_list[8],hrt_list[9]))
        con.commit()
    except Exception as msg:
        print(msg)
    finally:
        con.close()
################################################

################lb 입력################################
def ins_lb(id, lb_data):
    con = conn()
    try:
        cursor = con.cursor()

        sql = """INSERT INTO lb (lid, lb)   VALUES (%s, %s)"""
        cursor.execute(sql, (id, lb_data))
        con.commit()
    except Exception as msg:
        print(msg)
    finally:
        con.close()
###############################################################
