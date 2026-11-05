# Python_GUI_Tkinter

**中文** | [English](README_EN.md)

一个 Tkinter 桌面 GUI 入门示例集，覆盖 8 个常用部件（Widget）。每个脚本都是一个独立可运行的完整程序，配有详细的中文注释，适合零基础跟练。

## 环境要求

- Python 3.x
- Tkinter 为 Python 标准库内置模块，**无需 pip 安装**
  - Windows / macOS：官方安装包自带
  - Linux：如未安装，可执行 `sudo apt install python3-tk`

## 示例一览

| 文件 | 部件 | 演示要点 |
| --- | --- | --- |
| `Button.py` | Button 按钮 | `command=` 回调、点击切换标签文本 |
| `Canvas.py` | Canvas 画布 | 绘制直线 / 矩形 / 圆 / 弧、加载 GIF 图片、按钮控制图片移动 |
| `Checkbutton.py` | Checkbutton 复选框 | `IntVar` 变量绑定、按勾选组合更新标签样式 |
| `Entry.py` | Entry 输入框 | 登录界面、密码掩码 `show="*"`、账号密码校验 |
| `Listbox.py` | Listbox 列表框 | 增删列表项、读取当前选中项 |
| `Radiobutton.py` | Radiobutton 单选框 | 共享 `StringVar`、用字典映射简化 if/elif 判断 |
| `Scale.py` | Scale 滑块 | `after()` 定时器实现自动进度条、按区间变色、启动 / 停止控制 |
| `Text.py` | Text 文本框 | `"insert"`（光标处）与 `"end"`（末尾）两种插入方式对比 |

> 注：`main.py` 为 IDE 自动生成的模板文件，与本系列演示无关。

## 如何运行

每个脚本都是独立程序，没有统一入口，直接运行任意一个即可：

```bash
python Button.py
```

**注意**：运行 `Canvas.py` 时请从项目根目录执行，因为图片以相对路径 `./image/pic.gif` 引用。

## 涵盖知识点

- 8 大常用 Tkinter 部件的创建与配置
- `place()` 绝对定位布局
- `StringVar` / `IntVar` 变量绑定机制
- `command=` 事件回调
- `after()` 定时器实现动画与自动任务

## License

[MIT](LICENSE)
