import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500,
                     height=900,
                     bg = "black")
    canvas.pack()
    canvas.mainloop()
    