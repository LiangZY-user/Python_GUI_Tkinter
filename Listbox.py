"""
listbox是tkinter类中提供的的列表框部件，显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。
"""

import tkinter as tk
window = tk.Tk()
window.geometry("500x300") # 设置窗口大小
window.title("可选列表框") # 设置窗口标题

#添加一个标签
srt_var2 = tk.StringVar()
srt_var2.set("请选择") # 初始设置
lab1 = tk.Label(window,textvariable=srt_var2,bg="green",width=20,fg="black")
lab1.place(x=260,y=20)

# 创建可选列表框
srt_var = tk.StringVar()
srt_var.set(["Python","C++"])
listbox1 = tk.Listbox(window,width=30,height=6,listvariable=srt_var)
listbox1.place(x=20,y=20)

# 追加
list_var = ["PHP","Java","Ruby"]
for var in list_var:
    listbox1.insert(tk.END,var) # 在末尾追加

listbox1.insert(0,"C") # 在第一行插入C

# listbox1.delete(tk.END) # 删除末尾的元素
# listbox1.delete(2) # 删除下标 2 的元素

def show_lab():
    srt_var2.set((listbox1.get(listbox1.curselection()))) # 获取当前选中的文本

# 添加按钮
bt1 = tk.Button(window,text="显示",width=8,height=1,command=show_lab)
bt1.place(x=300,y=50)

window.mainloop()
