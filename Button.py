"""
 Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。
 按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。
 当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。
"""

# 因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面

# 导入库
import tkinter as tk

window = tk.Tk()
window.title('我的window窗口')
window.geometry('600x320')

# 设置标签1
lab1 = tk.Label(window,text="日期:2026/11/03",font=("微软雅黑",10,"bold"),width=16,height=2,bg = "green")
# 设置显示位置
lab1.place(x=0,y=0)

# 设置标签2
# 绑定tk字符串
str_var = tk.StringVar()
lab2 = tk.Label(window,textvariable=str_var,font=("微软雅黑",10,"bold"),width=32,height=2,bg = "red",fg="white")
# 设置显示位置
lab2.place(x=0,y=50)

def get_setvar():
    if str_var.get() == "":
        str_var.set("《《《 加载中 》》》")
    else:
        str_var.set("")

# 设置按钮
bt1 = tk.Button(window,text="显示文字",width=16,height=1,command=get_setvar)
bt1.place(x=50,y=100)

window.mainloop() # 进入循环