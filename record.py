# -*- coding: utf-8 -*-

import tkMessageBox
#每一个存款人信息
class Record:
    def __init__(self, name, password, money):
        self.m_name = name
        self.m_password = password
        self.m_money = money
        self.m_state = False

    #查询余额
    def search(self):
        if self.m_state == True:
            print "----------------------------------------"
            print " user:    |",
            print self.m_name
            print " money:   |",
            print self.m_money
            print "----------------------------------------"
        else:
            pass
        self.m_state = False

    #存款
    def save(self, money):
        if self.m_state == True:
            self.m_money += money
            print "----------------------------------------"
            print "You have secceed saved ",
            print money,
            print "Yuan. "
            print "----------------------------------------"
        else:
            pass
        self.m_state = False

    #取款
    def get(self, money):
        if self.m_state == True:
            if money <= self.m_money:
                self.m_money -= money
                print "----------------------------------------"
                print "You have secceed get ",
                print money,
                print "Yuan. "
                print "----------------------------------------"
            else:
                print "----------------------------------------"
                print "Your money is not enough. "
                print "----------------------------------------"
        else:
            pass
        self.m_state = False

    #修改密码
    def change_pwd(self):
        if self.m_state == True:
            print "----------------------------------------"
            print "input your old password: "
            print "----------------------------------------"
            password = raw_input()
            if int(password) == self.m_password:
                print "----------------------------------------"
                print "input your new password: "
                print "----------------------------------------"
                password1 = raw_input()
                print "----------------------------------------"
                print "input your new password again: "
                print "----------------------------------------"
                password2 = raw_input()
                if int(password1) == int(password2):
                    self.m_password = int(password1)
                    print "----------------------------------------"
                    print "You have succeed changed password. "
                    print "----------------------------------------"
                else:
                    print "----------------------------------------"
                    print "Your twice password is different."
                    print "----------------------------------------"
            else:
                print "----------------------------------------"
                print "Your password is wrong. "
                print "----------------------------------------"
        else:
            pass
        self.m_state = False

    #检查密码
    def check(self, password):
        if password == self.m_password:
            self.m_state = 1
            return True
        else:
            self.m_state = 0
            return False
    #随时准备安全保险
    def safe_deal(self):
        self.m_state = 0
    #查询程序
    def win_search(self):
        if self.m_state == True:
            msg_name_money = "username:  " + self.m_name + "\nmoney:      " + str(self.m_money)
            tkMessageBox.showinfo(title = "Search", message = msg_name_money)
        else:
            pass
        self.m_state = False
     #存钱程序，只处理核心程序，不管窗口
    def win_save(self, money):

        if self.m_state == True:
            self.m_money += money
            tkMessageBox.showinfo(title = "save", message = "You have secceed saved " + str(money) + " yuan.")
        else:
            pass
        self.m_state = False
    #取钱，只处理核心程序，不管窗口
    def win_get(self, money):
        if self.m_state == True:
            if money <= self.m_money:
                self.m_money -= money
                tkMessageBox.showinfo(title = "get", message = "You have succeed get " + str(money) + " yuan")
            else:
                tkMessageBox.showinfo(title = "get", message = "Your money is not enough.")
        else:
            pass
        self.m_state = False

        # 修改密码
    def win_change_pwd(self, changed_pwd):
        if changed_pwd[0] == self.m_password:
            if changed_pwd[1] == changed_pwd[2]:
                self.m_password = changed_pwd[1]
                tkMessageBox.showinfo(title = "change_pwd", message = "You have succeed changed the password")
            else:
                tkMessageBox.showinfo(title = "change_pwd", message = "Your twice input is different")
        else:
            tkMessageBox.showinfo(title = "change_pwd", message = "Your password is wrong")
        self.m_state = False

def test():
    obj = Record("herui", 123456, 1000)
    #print obj.m_money
    obj.m_state = True
    obj.search()
    obj.save(100)
    obj.search()
    obj.get(100)
    obj.search()
    obj.change_pwd()
#test()
