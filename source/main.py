'''
Created on 2017年4月20日

@author: zhangzhiyuan
'''
from WriteExcel import WriteExcel

from DBInfo import DBInfo
if __name__ == '__main__':
    dbinfo = DBInfo()
    order_sql = 'select * from data_service where status=1'
    operate_sql = 'select * from operate_steps where order_no=:order_no'
    # 选择配置文件的section
    db_group = 'ZZY'
    (conn, cur) = dbinfo.conndb(db_group)
    cur.execute(order_sql)
    rs = cur.fetchall()
    for r in rs:
        pr = {'order_no': r[0]}
        cur.execute(operate_sql, pr)
        operate_set = cur.fetchall()
        for operate_step in operate_set:
            conn1, cur1 = dbinfo.conndb(operate_step[4])
            cur1.execute(operate_step[2].replace(';', ''))
            data_set = cur1.fetchall()
            if operate_step[3] == "FILENAME":
                filename = data_set[0][0]
            elif operate_step[3] == "SHEETNAME":
                sheetname = data_set[0][0]
            elif operate_step[3] == "COLNAME":
                colname = data_set
            elif operate_step[3] == "DATA":
                path = dbinfo.getitem('EXCEL', 'path')
                we = WriteExcel(
                    path, filename, sheetname, colname, data_set)
                we.writefile()

    dbinfo.disconnalldb()
