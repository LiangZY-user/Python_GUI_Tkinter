# Python_GUI_Tkinter

**中文** | [English](README_EN.md)

一个 Tkinter 桌面 GUI 入门示例集，覆盖 10 个常用部件（Widget）。每个脚本都是独立可运行的完整程序，配有详细的中文注释，适合零基础跟练。

## 目录结构

```
Python_GUI_Tkinter/
├── Button.py           按钮
├── Canvas.py           画布
├── Checkbutton.py      复选框
├── Entry.py            单行输入框
├── Listbox.py          列表框
├── Radiobutton.py      单选框
├── Scale.py            滑块
├── Text.py             多行文本框
├── meun.py             菜单栏（文件名沿用现有拼写 meun，非 menu）
├── messageBox.py       消息弹窗
├── image/pic.gif       Canvas 示例图片（实际是 PNG，120×114）
├── main.py             PyCharm 自动生成的模板，与本系列无关
└── README_EN.md
```

## 环境要求

- Python 3.6+（源码使用 f-string；本机实测 Python 3.14 / Tk 9.0）
- Tkinter 为 Python 标准库内置模块，**无需 pip 安装**
  - Windows / macOS：官方安装包自带
  - Linux：如未安装，执行 `sudo apt install python3-tk`
- 自检是否可用：

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```

## 示例一览

| 文件 | 部件 | 演示要点 |
| --- | --- | --- |
| `Button.py` | Button 按钮 | `StringVar` + `textvariable` 绑定，`command=` 回调点击切换标签文字 |
| `Canvas.py` | Canvas 画布 | 直线 / 矩形 / 椭圆 / 扇形弧；按 `__file__` 定位加载图片；按钮调用 `move()` 移动图元 |
| `Checkbutton.py` | Checkbutton 复选框 | `IntVar` 记录勾选状态 + `textvariable`，用字典映射替代 if/elif 配色 |
| `Entry.py` | Entry 输入框 | 登录校验（账号 `admin` / 密码 `123456`）、`show="*"` 掩码、`.get()` 取值 |
| `Listbox.py` | Listbox 列表框 | `listvariable` 初始化、`insert(tk.END)` / `insert(0, ...)` 插入、`curselection()` 取选中项（`delete` 示例已注释，可自行放开） |
| `Radiobutton.py` | Radiobutton 单选框 | 共享 `StringVar`、`value` 保证互斥、字典映射简化判断 |
| `Scale.py` | Scale 滑块 | `from_` / `to` / `resolution` / `tickinterval` 参数、`after(50, ...)` 自循环动画、按区间变色、启动 / 停止控制 |
| `Text.py` | Text 文本框 | `"insert"`（光标处）与 `"end"`（末尾追加）两种插入方式对比 |
| `meun.py` | Menu 菜单 | `tearoff=0` 下拉菜单、`add_cascade` 挂载子菜单、`win.config(menu=...)` 装配菜单栏 |
| `messageBox.py` | messageBox 弹窗 | 按钮触发 `showinfo` / `showwarning` 消息框 |

> 注：`main.py` 为 PyCharm 自动生成的模板文件，与本系列演示无关。

## 如何运行

每个脚本都是独立程序，没有统一入口，直接运行任意一个即可：

```bash
python Button.py
```

所有脚本都不依赖工作目录 —— `Canvas.py` 的图片路径基于脚本自身位置解析，在任何目录下启动都能正常加载。

VS Code 中若提示 `No module named 'tkinter'`，按 `Ctrl+Shift+P` → **Python: Select Interpreter**，选择一个带 Tk 的解释器即可。

## 常见问题

| 现象 | 处理 |
| --- | --- |
| `ModuleNotFoundError: No module named 'tkinter'` | 当前解释器不带 Tk，换一个官方安装包的解释器 |
| `_tkinter.TclError: couldn't open ".../pic.gif"` | 图片路径不对，确认 `image/pic.gif` 存在且用的是 `IMG_PATH` 写法 |
| 图片区域空白但不报错 | `PhotoImage` 未被变量持有而被回收，需用变量接收 |

## 涵盖知识点

- 10 个常用 Tkinter 部件的创建与配置
- `place()` 绝对定位布局
- `StringVar` / `IntVar` 变量绑定（`textvariable` / `listvariable` / `variable`）
- `command=` 事件回调，含 `lambda` 传参与带参回调
- `after()` 定时器实现动画与自动任务
- Canvas 图元、坐标模型与 `__file__` 锚定资源路径

## License

[MIT](LICENSE) © 2026 LiangZY-user
