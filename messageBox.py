"""
messageBox 消息框，用于显示你应用程序的消息框。(Python2中为tkMessagebox) 其实这里的messageBox就是我们平时看到的弹窗。 我们首先需要定义一个触发功能，来触发这个弹窗 这里我们就放上以前学过的button按钮 通过触发功能 调用messagebox吧 点击button按钮就会弹出提示对话框。
"""

import tkinter as tk
import tkinter.messagebox as messagebox

win = tk.Tk()
win.title("messageBox")
win.geometry("400x300")
win.resizable(0, 0)

def show_message():
    messagebox.showinfo(title="提示", message="这是一个提示信息")

tk.Button(win, text="提示", command=show_message).place(x=160, y=100)
def show_warning():
    messagebox.showwarning(title="警告", message="这是一个警告信息")

tk.Button(win, text="警告", command=show_warning).place(x=200, y=100)

win.mainloop()
