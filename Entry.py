"""
Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)
"""


import tkinter as tk

window = tk.Tk()
window.title("登录界面")
window.geometry("360x180")
#  关键：锁住窗口，禁止缩放
window.resizable(False, False)

# 设置标签1
lab1 = tk.Label(window,text="用户名",font=("微软雅黑",10,"bold"),width=6,height=1)
# 设置显示位置
lab1.place(x=60,y=10)

entry1 = tk.Entry(window,show=None) # 明文显示
entry1.place(x=120,y=10)

# 设置标签2
lab2 = tk.Label(window,text="密  码",font=("微软雅黑",10,"bold"),width=6,height=1)
# 设置显示位置
lab2.place(x=60,y=32)

# 设置标签3
str_var = tk.StringVar()
lab3 = tk.Label(window,textvariable=str_var,font=("微软雅黑",10,"bold"),fg="red")
# 设置显示位置
lab3.place(x=100,y=100)

entry2 = tk.Entry(window,show="*") # 密钥显示
entry2.place(x=120,y=32)

def get_button():
    if entry1.get() !=  "admin" or entry2.get() != "123456": # entry1.get() 获取输入框中的文本
        str_var.set("用户名或密码错误，请重新输入")
    else:
        str_var.set("登录成功，欢迎光临")

# 按钮
bt1 = tk.Button(window,text="登录账户",font=("微软雅黑",10,"bold"),width=6,height=1,command=get_button)
bt1.place(x=160,y=60)

window.mainloop()
