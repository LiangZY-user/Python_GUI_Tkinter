# Python_GUI_Tkinter

[中文](README.md) | **English**

A beginner-friendly collection of Tkinter desktop GUI examples covering 8 commonly used widgets. Each script is a complete, standalone program with detailed Chinese comments in the source code, perfect for learning from scratch.

## Requirements

- Python 3.x
- Tkinter ships with the Python standard library — **no pip install needed**
  - Windows / macOS: bundled with the official installer
  - Linux: install via `sudo apt install python3-tk` if missing

## Examples

| File | Widget | What It Demonstrates |
| --- | --- | --- |
| `Button.py` | Button | `command=` callback, toggling label text on click |
| `Canvas.py` | Canvas | Drawing lines / rectangles / ovals / arcs, loading a GIF, moving an image via button |
| `Checkbutton.py` | Checkbutton | `IntVar` binding, updating label style by checked combination |
| `Entry.py` | Entry | Login form, password masking with `show="*"`, credential validation |
| `Listbox.py` | Listbox | Adding / deleting items, reading the current selection |
| `Radiobutton.py` | Radiobutton | Shared `StringVar`, replacing if/elif chains with a dict mapping |
| `Scale.py` | Scale | Auto-running progress bar via `after()` timer, range-based colors, start / stop control |
| `Text.py` | Text | Comparing `"insert"` (at cursor) vs `"end"` (append) insertion |

> Note: `main.py` is an IDE-generated template file and is unrelated to these demos.

## How to Run

Each script is an independent program — there is no unified entry point. Just run any of them directly:

```bash
python Button.py
```

**Note**: Run `Canvas.py` from the project root directory, since the image is referenced by the relative path `./image/pic.gif`.

## Topics Covered

- Creating and configuring 8 common Tkinter widgets
- Absolute positioning with `place()`
- Variable binding with `StringVar` / `IntVar`
- Event callbacks via `command=`
- Animation and scheduled tasks with `after()`

## License

[MIT](LICENSE)
