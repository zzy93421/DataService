'''
Created on 2017年4月18日

@author: zhangzhiyuan
'''

import configparser


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

    def getitem(self, sec, opt):
        '''
        获取配置项函数
        '''
        return self.cp.get(sec, opt)

if __name__ == '__main__':
    db = DBInfo()
    print(db.getitem('XGP1', 'host'))
