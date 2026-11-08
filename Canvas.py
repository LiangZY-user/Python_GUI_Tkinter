"""
Canvas 画布提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
"""
import os
import tkinter as tk

# 图片路径要基于本文件所在目录，否则换个工作目录运行就会报
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "image", "pic.gif")

window = tk.Tk()
window.title("Canvas")
window.geometry("800x600")
window.resizable(width=False, height=False)

# 在窗口创建画布
can1 = tk.Canvas(window, width=400, height=300,bg="pink")

# 画直线
# fill 设置线条颜色
# 以画布为边界，不是以窗口
can1_line = can1.create_line(0,30,80,30,width = 2,fill = "yellow")
# 画矩形
can1_rec = can1.create_rectangle(60,60,100,100,fill = "red")
# 画圆形
can1_garden = can1.create_oval(100,100,200,200,fill = "blue")
# 花圆弧
can1_arc = can1.create_arc(10,200,100,300,fill = "white",start = 0 ,extent = 90)
# t填充图片
can1_img = tk.PhotoImage(file=IMG_PATH)
_img = can1.create_image(200,10,image=can1_img,anchor = tk.NW)

can1.place(x=200, y=20) # 刷新到画布上
#按钮移动
def move():  # 定义一个名为move的函数
    can1.move(_img,0,2)  # 调用can1对象的move方法，将_img对象在垂直方向向下移动2个单位，水平方向保持不变（0）
tk.Button(window, text="MOVE", bg="pink", width=6,command=move).place(x=300, y=330)

window.mainloop()