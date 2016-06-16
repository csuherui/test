# -*- coding: utf-8 -*-

import MySQLdb
from record import *
from collections import deque
class Database():
    def __init__(self):
        # 这两步用来连接数据库
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='herui_mysql',
        )
        self.cur = self.conn.cursor()
        #存款人信息集
        #说明:从数据库中调取数据，但是还是通过内存来实现管理的，不直接在数据库层面操作
        query1 = "select name,  password, money from first_table;"
        self.cur.execute(query1)
        results = self.cur.fetchall()
        self.data_queue = deque([])
        for i in range(len(results)):
            self.data_queue.append(Record(results[i][0], results[i][1], results[i][2]))
        #存款总人数
        self.data_length = len(self.data_queue)
        #存款人名单集
        self.data_name = []
        for i in range(self.data_length):
            self.data_name.append(self.data_queue[i].m_name)
    def add_data(self, record):
        self.data_queue.append(record)

    def data_print(self):
        for i in range(len(self.data_queue)):
            print self.data_queue[i].m_name,
            print " ",
            print self.data_queue[i].m_password,
            print " ",
            print self.data_queue[i].m_money
    def post(self, name1, name2, money):
        pass


def test():
    obj = Database()
    record1 = Record("xiaobai", 111111, 0)
    obj.add_data(record1)
    obj.data_print()

#test()
