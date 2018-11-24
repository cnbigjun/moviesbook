import pymysql

def connect_wxremit_db():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123123',
                           database='crm',
                           charset='utf8',
    )
def query_country_name():
    sql_str = "select * from sys_user where user_id=%d"
    con = connect_wxremit_db()
    # 设置游标卡尺 让返回字典型数据  //查询
    cur = con.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql_str %(5))
    rows = cur.fetchone()

    # 增加 修改  删除 都是一样的
    sql_insert = "INSERT INTO sys_user(user_code,\
         user_name, user_password, user_state)\
         VALUES ('%s', '%s', '%s', '%s')"
    try:
        cur.execute(sql_insert % (rows['user_code'],rows['user_name'],rows['user_password'],rows['user_state']))
        con.commit()
    except:
        con.rollback()

    cur.close()
    con.close()
query_country_name()