# Scale： 尺度（拉动条），允许你通过滑块来设置一数字值。

import tkinter as tk
win = tk.Tk()
win.geometry("600x300")
win.title("进度条")

# 标签
lab1 = tk.Label(win,text="当前进度:0.0%",bg="red",width=28,height=1,fg = "black")
lab1.place(x=120,y=20)


# 需要一个参数
def print_scale(v):
    var = int(float(v))
    if  0 <= var <= 30:
        lab1.config(text=f"当前进度:{v}%",bg = "red")
    elif 31 <= var <= 70:
        lab1.config(text=f"当前进度:{v}%", bg="yellow")
    elif 71 <= var <= 100:
        lab1.config(text=f"当前进度:{v}%", bg="green")

# 进度条
scale1 = tk.Scale(win, label="进度条", from_=0, to=100,length=400,orient=tk.HORIZONTAL,showvalue=False
                  ,tickinterval=10,resolution=0.1,bg="yellow",command=print_scale)
scale1.place(x=120,y=60)

after = None
is_running = False
# 自动运行函数
def auto_run():
    global after, is_running
    now = scale1.get()
    if now >= 100:
        scale1.set(0)   # 到100归零
    else:
        scale1.set(now + 0.2)
        # 每隔50ms调用自己，持续跑动
    if is_running:
        after = win.after(50, auto_run)
        is_running = True


def my_start():
    global after, is_running
    if after is None:
        is_running = True
        auto_run()
def my_stop():
    global after, is_running
    if after is not None :
        is_running = False
        scale1.set(scale1.get())

bt1 = tk.Button(win, text="启动按钮", width=10, height=1, bg = "green", command=my_start)
bt1.place(x=160,y=160)

bt2 = tk.Button(win, text="停止按钮", width=10, height=1, bg = "red", command=my_stop)
bt2.place(x=260,y=160)

win.mainloop()