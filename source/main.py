'''
Created on 2017年4月20日

@author: zhangzhiyuan
'''
import cx_Oracle
from DBInfo import DBInfo
if __name__ == '__main__':
    dbinfo = DBInfo()
    '''tns = cx_Oracle.makedsn(
        dbinfo.getitem('ZZY', 'host'), dbinfo.getitem('ZZY', 'port'), dbinfo.getitem('ZZY', 'service'))
    db = cx_Oracle.connect(
        dbinfo.getitem('ZZY', 'user'), dbinfo.getitem('ZZY', 'password'), tns)
    cr = db.cursor()
    order_sql = 'select * from data_service where status=1'
    data_sql = 'select * from operate_steps where order_no=:order_no'
    cr.execute(order_sql)
    rs = cr.fetchall()
    for r in rs:
        pr = {'order_no': r[0]}
        cr.execute(data_sql, pr)
        data_set = cr.fetchall()
        for data in data_set:
            print(data)
    '''
    order_sql = 'select * from data_service where status=1'
    operate_sql = 'select * from operate_steps where order_no=:order_no'
    db_group = 'ZZY'
    (conn, cur) = dbinfo.conndb(db_group)
    cur.execute(order_sql)
    rs = cur.fetchall()
    for r in rs:
        pr = {'order_no': r[0]}
        cur.execute(operate_sql, pr)
        operate_set = cur.fetchall()
        for operate_step in operate_set:
            print(operate_step)

    dbinfo.disconnalldb()
