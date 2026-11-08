"""
Menu 菜单条，用来实现下拉和弹出式菜单，点下菜单后弹出的一个选项列表,用户可以从中选择
"""

import tkinter as tk

win = tk.Tk()
win.title("菜单")
win.geometry("400x300")
win.resizable(0, 0)

# 添加一个标签，用来显示菜单的选择结果
lab1 = tk.Label(win, text=" red ", font=("微软雅黑", 10, "bold"), width=6, height=1, fg="blue", bg="pink")
lab1.place(x=160, y=100)

# 创建菜单
meun1 = tk.Menu(win)

filemenu = tk.Menu(meun1, tearoff=0)  # 创建一个下拉菜单
filemenu.add_command(label="新建文件", command=lambda: lab1.config(text="新建文件"))  # 添加菜单项
filemenu.add_command(label="保存文件", command=lambda: lab1.config(text="保存文件"))  # 菜单项

setmenu = tk.Menu(meun1, tearoff=0)  # 创建一个下拉菜单
setmenu.add_command(label="设置", command=lambda: lab1.config(text="设置"))

meun1.add_cascade(label="菜单", menu=filemenu)  # 将下拉菜单添加到菜单栏中
meun1.add_cascade(label="设置", menu=setmenu)  # 将下拉菜单添加到菜单栏中
win.config(menu=meun1)  # 将菜单栏添加到窗口中
win.mainloop()