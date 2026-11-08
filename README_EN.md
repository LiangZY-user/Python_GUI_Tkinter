# Python_GUI_Tkinter

[中文](README.md) | **English**

A beginner-friendly collection of Tkinter desktop GUI examples covering 10 commonly used widgets. Each script is a complete, standalone program with detailed Chinese comments in the source code, perfect for learning from scratch.

## Project Structure

```
Python_GUI_Tkinter/
├── Button.py           Button
├── Canvas.py           Canvas
├── Checkbutton.py      Checkbutton
├── Entry.py            Entry
├── Listbox.py          Listbox
├── Radiobutton.py      Radiobutton
├── Scale.py            Scale
├── Text.py             Text
├── meun.py             Menu (filename keeps the existing spelling "meun")
├── messageBox.py       Message boxes
├── image/pic.gif       Image used by Canvas (actually a PNG, 120×114)
├── main.py             PyCharm-generated template, unrelated to these demos
└── README_EN.md
```

## Requirements

- Python 3.6+ (the code uses f-strings; tested on Python 3.14 / Tk 9.0)
- Tkinter ships with the Python standard library — **no pip install needed**
  - Windows / macOS: bundled with the official installer
  - Linux: install via `sudo apt install python3-tk` if missing
- Verify it is available:

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```

## Examples

| File | Widget | What It Demonstrates |
| --- | --- | --- |
| `Button.py` | Button | `StringVar` + `textvariable` binding, toggling label text via `command=` callback |
| `Canvas.py` | Canvas | Lines / rectangles / ovals / arc; loading an image via a `__file__`-based path; moving an item with `move()` |
| `Checkbutton.py` | Checkbutton | `IntVar` state + `textvariable`, dict mapping instead of if/elif for colors |
| `Entry.py` | Entry | Login check (user `admin` / password `123456`), masking with `show="*"`, reading values via `.get()` |
| `Listbox.py` | Listbox | `listvariable` initialization, `insert(tk.END)` / `insert(0, ...)`, reading selection with `curselection()` (`delete` samples are commented out) |
| `Radiobutton.py` | Radiobutton | Shared `StringVar`, mutually exclusive `value`, dict mapping to skip if/elif chains |
| `Scale.py` | Scale | `from_` / `to` / `resolution` / `tickinterval` options, self-looping `after(50, ...)` animation, range-based colors, start / stop control |
| `Text.py` | Text | Comparing `"insert"` (at cursor) vs `"end"` (append) |
| `meun.py` | Menu | `tearoff=0` dropdowns, `add_cascade` for submenus, attaching the bar with `win.config(menu=...)` |
| `messageBox.py` | messageBox | Buttons triggering `showinfo` / `showwarning` dialogs |

> Note: `main.py` is a PyCharm-generated template file and is unrelated to these demos.

## How to Run

Each script is an independent program — there is no unified entry point. Just run any of them directly:

```bash
python Button.py
```

None of the scripts depend on the working directory — `Canvas.py` resolves its image relative to the script file itself, so it loads correctly no matter where you launch it from.

If VS Code reports `No module named 'tkinter'`, press `Ctrl+Shift+P` → **Python: Select Interpreter** and pick an interpreter that ships with Tk.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `ModuleNotFoundError: No module named 'tkinter'` | The selected interpreter lacks Tk; switch to one from the official installer |
| `_tkinter.TclError: couldn't open ".../pic.gif"` | Wrong image path; make sure `image/pic.gif` exists and the `IMG_PATH` approach is used |
| Image area blank but no error | The `PhotoImage` was garbage-collected; keep a reference in a variable |

## Topics Covered

- Creating and configuring 10 common Tkinter widgets
- Absolute positioning with `place()`
- Variable binding with `StringVar` / `IntVar` (`textvariable` / `listvariable` / `variable`)
- Event callbacks via `command=`, including `lambda` and callbacks with arguments
- Animation and scheduled tasks with `after()`
- Canvas items, the coordinate model, and `__file__`-anchored resource paths

## License

[MIT](LICENSE) © 2026 LiangZY-user
