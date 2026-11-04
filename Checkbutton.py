"""
Checkbutton：代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换，选择和取消选择
"""

import tkinter as tk
win = tk.Tk()
win.geometry("500x300")
win.title("Checkbutton")
win.resizable(False,False)

# 标签
srt_var1 = tk.StringVar()
srt_var1.set("PYTHON")
srt_var2 = tk.StringVar()
srt_var2.set("JAVA")

lab1 = tk.Label(win,text="这是一个标签",bg="white",width=20,height=2)
lab1.place(x=120,y=20)

# 定义两个变量接受返回值
var1 = tk.IntVar()
var2 = tk.IntVar()
color_var = {"PYTHON":"green","JAVA":"yellow"}

def get_checkbutton():
    if var1.get() == 1 and var2.get() == 0:
        lab1.config(text ="I LOVE "+srt_var1.get(),bg = color_var[srt_var1.get()],font=("Arial", 12,"bold"))
    elif var1.get() == 0 and var2.get() == 1:
        lab1.config(text="I LOVE "+srt_var2.get(), bg=color_var[srt_var2.get()],font=("Arial", 12,"bold"))
    else:
        lab1.config(text="这是一个标签",bg="white")
# 选项
check1 = tk.Checkbutton(win, textvariable=srt_var1, variable=var1, onvalue=1, offvalue=0, font=("Arial", 12), bg="green"
                        , width=10, height=1, command=get_checkbutton)
check1.place(x=130, y=70)
check2 = tk.Checkbutton(win, textvariable=srt_var2, variable=var2, onvalue=1, offvalue=0, font=("Arial", 12), bg="yellow"
                        , width=10, height=1,command=get_checkbutton)
check2.place(x=130, y=100)

win.mainloop()