"""
Radiobutton：代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。
"""

import tkinter as tk
window = tk.Tk()
window.title("Radiobutton")
window.geometry("400x300")
window.resizable(False,False)

# 标签
srt_var = tk.StringVar()
srt_var.set(" ")
lab1 = tk.Label(window,text="empty",bg="white",width=20,height=1)
lab1.place(x=120,y=20)

# def print_srt():
#     if srt_var.get() == "A":
#         lab1.config(bg="green")
#     elif srt_var.get() == "B":
#         lab1.config(bg="red")
#     elif srt_var.get() == "C":
#         lab1.config(bg="yellow")
#     lab1.config(text="选项"+srt_var.get())

color_var = {"A":"green","C":"yellow","B":"red"}

def print_srt():
    lab1.config(text="选项"+srt_var.get())
    lab1.config(bg=color_var[srt_var.get()])

# Radiobutton
rad1 = tk.Radiobutton(window,text="选项A",variable=srt_var,value="A",bg="green",command=print_srt)
rad1.place(x=120,y=100)
rad2 = tk.Radiobutton(window,text="选项B",variable=srt_var,value="B",bg="red",command=print_srt)
rad2.place(x=120,y=140)
rad3 = tk.Radiobutton(window,text="选项C",variable=srt_var,value="C",bg="yellow",command=print_srt)
rad3.place(x=120,y=180)

window.mainloop()