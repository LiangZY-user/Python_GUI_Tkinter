# Scale： 尺度（拉动条），允许你通过滑块来设置一数字值。

import tkinter as tk
win = tk.Tk()
win.geometry("600x300")
win.title("进度条")
win.resizable(False, False)
# 标签
lab1 = tk.Label(win,text="当前进度:0.0%",bg="red",width=28,height=1,fg = "black")
lab1.place(x=120,y=20)

# 需要一个参数
def print_scale(v):
    # 将输入值转换为浮点数，然后转换为整数
    var = int(float(v))
    # 判断数值范围并设置相应的背景颜色和文本
    if  0 <= var <= 30:
        # 当进度在0-30之间时，设置背景为红色
        lab1.config(text=f"当前进度:{v}%",bg = "red")
    elif 31 <= var <= 70:
        # 当进度在31-70之间时，设置背景为粉色
        lab1.config(text=f"当前进度:{v}%", bg="pink") # pink 粉色
    elif 71 <= var <= 100:
        # 当进度在71-100之间时，设置背景为绿色
        lab1.config(text=f"当前进度:{v}%", bg="green")

# 进度条
"""
from_=0, to=100 进度条从起点from_到终点to
length=400 进度条显示长度
orient=tk.HORIZONTAL 代表方向；HORIZONTAL = 水平 `orient=tk.VERTICAL` 垂直滑块，上下拉动
showvalue=False 是否在进度条上显示数值 ，False 不显示 True 显示
tickinterval=10 是10的间隔显示进度条
resolution=0.1 精度
"""
scale1 = tk.Scale(win, label="进度条", from_=0, to=100,length=400,orient=tk.HORIZONTAL,showvalue=False
                  ,tickinterval=10,resolution=0.1,bg="yellow",command=print_scale)
scale1.place(x=120,y=60)

after_id = None # 禁止点击启动按钮加速
is_running = False # 是否在运行
# 自动运行函数
def auto_run():
    global after_id, is_running
    now = scale1.get()
    if now >= 100:
        scale1.set(0)   # 到100归零
    else:
        scale1.set(now + 0.2)
    # 每隔50ms调用自己，持续跑动
    if is_running:
        after_id = win.after(50, auto_run)

def my_start():
    global after_id, is_running
    is_running = True
    if is_running:
        if after_id is None:
            auto_run()
def my_stop():
    global is_running, after_id
    is_running = False
    if not is_running:
        after_id = None
        scale1.set(scale1.get())


bt1 = tk.Button(win, text="启动按钮", width=10, height=1, bg = "green", command=my_start)
bt1.place(x=160,y=160)

bt2 = tk.Button(win, text="停止按钮", width=10, height=1, bg = "red", command=my_stop)
bt2.place(x=260,y=160)

win.mainloop()