'''
Created on 2017年4月18日

@author: zhangzhiyuan
'''

import configparser
import cx_Oracle


class DBInfo:
    '''
    本类用于存储与DB相关的信息
    '''

    def __init__(self):
        '''
        初始化函数
        '''
        self.file = '..//conf//config.ini'
        self.cp = configparser.SafeConfigParser()
        self.cp.read(self.file)
        self.dbconn_pool = {}

    def getitem(self, sec, opt):
        '''
        获取配置项函数
        '''
        return self.cp.get(sec, opt)

    def conndb(self, db_group):
        '''
        建立数据库连接
        '''
        if db_group in self.dbconn_pool.keys():
            return (self.dbconn_pool[db_group]['conn'], self.dbconn_pool[db_group]['cur'])
        else:
            tns = cx_Oracle.makedsn(self.getitem(db_group, 'host'), self.getitem(
                db_group, 'port'), self.getitem(db_group, 'service'))
            user = self.getitem(db_group, 'user')
            pwd = self.getitem(db_group, 'password')
            conn = cx_Oracle.connect(user, pwd, tns)
            cur = conn.cursor()
            self.dbconn_pool[db_group] = {'conn': conn, 'cur': cur, }
            return (conn, cur)
            pass

    def disconndb(self, db_group):
        '''
        断开数据库连接
        '''
        if self.dbconn_pool.has_key(db_group):
            self.dbconn_pool[db_group]['cur'].close()
            self.dbconn_pool[db_group]['conn'].commit()
            self.dbconn_pool[db_group]['conn'].close()
            del self.dbconn_pool[db_group]

    def disconnalldb(self):
        '''
        断开已建立的所有数据库连接
        '''
        for key in self.dbconn_pool.keys():
            self.dbconn_pool[key]['cur'].close()
            self.dbconn_pool[key]['conn'].commit()
            self.dbconn_pool[key]['conn'].close()
            pass

if __name__ == '__main__':
    db = DBInfo()
    print(db.getitem('XGP1', 'host'))
