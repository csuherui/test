#coding: utf-8
'''
author:   HeRui
company:  Central South University
e-mail:   15009228478@163.com
'''
#先面向过程写吧

import Tkinter as tk
import tkMessageBox
import getpass
import database
import os

root = tk.Tk()

msg_name = tk.StringVar()   #把信息作为全局变量有多危险！！！！
msg_pwd = tk.StringVar()

#临时程序，暂时没什么用
def Search():
    print "Search"
    print datas.cur.execute("select * from first_table;")
    results = datas.cur.fetchall()
    print results


#根据输入的密码决定是否打开权限,然后决定执行哪一步
def CmdInputMessage(win1, num_method):
    win1.destroy()
    temp_message = database.Record(msg_name.get(), int(msg_pwd.get()), 0)
    # 校对名字
    try:
        id_name = datas.data_name.index(temp_message.m_name)
    except:
        id_name = -1
    # 校对密码
    if id_name == -1:
        pass
    else:
        judge = datas.data_queue[id_name].check(temp_message.m_password)
        if judge == False:
            id_name = -1
    if num_method == 1:
        Search1(id_name)
    elif num_method == 2:
        Get(id_name)
    elif num_method ==3:
        Save(id_name)
    elif num_method == 5:
        Change_pwd(id_name)

#输入密码，然后决定是否打开权限
#界面程序
def InputMessage(num_method):
    win1 = tk.Toplevel(root)
    win1_frame = tk.Frame(win1)
    win1_frame.pack(padx = 20, pady = 10)
    win1_label1 = tk.Label(win1_frame, text = "username:  ")
    win1_label1.grid(row = 1, column = 0)
    win1_label2 = tk.Label(win1_frame, text = "password:  ")
    win1_label2.grid(row = 2, column = 0)
    win1_e1 = tk.Entry(win1_frame, textvariable = msg_name)
    win1_e1.grid(row = 1, column = 1)
    win1_e2 = tk.Entry(win1_frame, textvariable = msg_pwd, show = '*')
    win1_e2.grid(row = 2, column = 1)
    win1_cmd1 = tk.Button(win1_frame, text = "OK", command = lambda:CmdInputMessage(win1, num_method))
    win1_cmd1.grid(row = 3)
    msg_name.set("")
    msg_pwd.set("")
#查询信息信息提示程序
def Search1(id_name):
    if id_name == -1:
        pass
    else:
        datas.data_queue[id_name].win_search()

#存钱窗口程序
def Save(id_name):
    if id_name == -1:
        pass
    else:
        win2 = tk.Toplevel(root)
        win2_frame = tk.Frame(win2)
        win2_frame.pack(padx = 20, pady = 10)
        win2.title = "Please input how much you save:"
        var_money = tk.StringVar()
        win2_e1 = tk.Entry(win2_frame, textvariable = var_money)
        win2_e1.pack()
        win2_cmd1 = tk.Button(win2_frame, text = "OK", command = lambda:save_sub1(win2, id_name, var_money))
        win2_cmd1.pack()
#存钱窗口程序按钮调用程序
def save_sub1(win2, id_name, var_money):
    win2.destroy()
    datas.data_queue[id_name].win_save(int(var_money.get()))
    #操作数据库
    data_temp = datas.data_queue[id_name]
    sql_alter = "UPDATE first_table SET money = " + str(data_temp.m_money) +" WHERE name = '" + str \
        (data_temp.m_name) + "';"
    datas.cur.execute(sql_alter)
    datas.conn.commit()
#取钱窗口程序
def Get(id_name):
    if id_name == -1:
        pass
    else:
        win3 = tk.Toplevel(root)
        win3_frame = tk.Frame(win3)
        win3_frame.pack(padx=20, pady=10)
        win3.title = "Please input how much you get:"
        var_money = tk.StringVar()
        win3_e1 = tk.Entry(win3_frame, textvariable=var_money)
        win3_e1.pack()
        win3_cmd1 = tk.Button(win3_frame, text="OK", command=lambda: get_sub1(win3, id_name, var_money))
        win3_cmd1.pack()
#取钱窗口程序调用按钮调用程序
def get_sub1(win3, id_name, var_money):
    win3.destroy()
    datas.data_queue[id_name].win_get(int(var_money.get()))
    #操作数据库
    data_temp = datas.data_queue[id_name]
    sql_alter = "UPDATE first_table SET money = " + str(data_temp.m_money) + " WHERE name = '" + str( \
                data_temp.m_name) + "';"
    datas.cur.execute(sql_alter)
    datas.conn.commit()
#改密码窗口程序
def Change_pwd(id_name):
    print id_name
    if id_name == -1:
        pass
    else:
        win4 = tk.Toplevel(root)
        win4_frame = tk.Frame(win4)
        win4_frame.pack(padx = 40, pady = 20)
        win4.title = "Please input your message:"
        var_pwd1 = tk.StringVar()
        var_pwd2 = tk.StringVar()
        var_pwd3 = tk.StringVar()
        win4_l1 = tk.Label(win4_frame, text = "old password       ")
        win4_l1.grid(row = 0, column = 0)
        win4_l2 = tk.Label(win4_frame, text="new password         ")
        win4_l2.grid(row = 1, column = 0)
        win4_l3 = tk.Label(win4_frame, text="ensure new password  ")
        win4_l3.grid(row = 2, column = 0)
        win4_e1 = tk.Entry(win4_frame, textvariable = var_pwd1, show = '*')
        win4_e1.grid(row = 0, column = 1)
        win4_e2 = tk.Entry(win4_frame, textvariable = var_pwd2, show = '*')
        win4_e2.grid(row = 1, column = 1)
        win4_e3 = tk.Entry(win4_frame, textvariable = var_pwd3, show = '*')
        win4_e3.grid(row = 2, column = 1)
        win4_cmd1 = tk.Button(win4_frame, text="OK", command=lambda:change_pwd_sub1(win4, id_name, var_pwd1, var_pwd2, var_pwd3))
        win4_cmd1.grid(row = 3, column = 0)
#改密码窗口程序按钮调用程序
def change_pwd_sub1(win4, id_name, var_pwd1, var_pwd2, var_pwd3):
    win4.destroy()
    changed_pwd = []
    changed_pwd.append(int(var_pwd1.get()))
    changed_pwd.append(int(var_pwd2.get()))
    changed_pwd.append(int(var_pwd3.get()))
    datas.data_queue[id_name].win_change_pwd(changed_pwd)
    #操作数据库
    data_temp = datas.data_queue[id_name]
    sql_alter = "UPDATE first_table SET password = " + str(data_temp.m_password) + " WHERE name = '" + str(
        data_temp.m_name) + "';"
    datas.cur.execute(sql_alter)
    datas.conn.commit()
#退出程序
def WinQuit():
    datas.cur.close()
    datas.conn.close()
    root.destroy()












#主程序
root.title("Herui ACM bank")
datas = database.Database()
frame = tk.Frame(root)
frame.pack(padx = 20, pady = 10)
label = tk.Label(frame, text = "Welcome to Herui ACM bank")
label.grid(row = 0, column = 1)
cmd1 = tk.Button(frame, text = "search", command = lambda:InputMessage(1), width = 5, height = 2)
cmd1.grid(row = 1, column = 0)
cmd2 = tk.Button(frame, text = "get", command = lambda:InputMessage(2), width = 5, height = 2)
cmd2.grid(row = 1, column = 1)
cmd3 = tk.Button(frame, text = "save", command = lambda:InputMessage(3), width = 5, height = 2)
cmd3.grid(row = 1, column = 2)
cmd5 = tk.Button(frame, text = "post", command = Search, width = 5, height = 2)
cmd5.grid(row = 2, column = 0)
cmd5 = tk.Button(frame, text = "change\npassword", command = lambda:InputMessage(5), width = 5, height = 2)
cmd5.grid(row = 2, column = 1)
cmd6 = tk.Button(frame, text = "quit", command = WinQuit, width = 5, height = 2)
cmd6.grid(row = 2, column = 2)




root.mainloop()
