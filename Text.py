"""
Text是tkinter类中提供的的一个多行文本区域，显示多行文本，
可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)，
格式化文本显示，允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。
"""

# 因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面

import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("文本框")
window.resizable(False, False)

# 创建输入框
ent1 = tk.Entry(window,show=None,width=30)
ent1.place(x=60,y=10)

def get_inster():
    var = ent1.get()
    text1.insert("insert",var) # 在文本框鼠标处，插入文本

def get_end():
    var = ent1.get()
    text1.insert("end",var)# 在文本框末尾处，拼接文本

# 添加按钮
bt1 = tk.Button(window,text="inster",width=8,height=1,command=get_inster)
bt1.place(x=60,y=60)

#
bt2 = tk.Button(window,text="end",width=8,height=1,command=get_end)
bt2.place(x=140,y=60)

#创建文本框
text1 = tk.Text(window,height=5,width=30,bg="green",fg="black",font=("微软雅黑",10,"bold"))
text1.place(x=60,y=120)

window.mainloop()