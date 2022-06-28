import tkinter as tk

def key_down(event):
    global key
    key = event.keysym #key event
    #print(f"{key}キーが押されました")

def key_up():
    global key
    key = "" #空

def main_proc():
    global cx,cy
    if key == "Up"    : cy -= 20
    if key == "Down"  : cy += 20
    if key == "Left"  : cx -= 20
    if key == "Right" : cx += 20
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()    #ウインドウ
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, 
                     height=900,
                     bg = "black")
    tori = tk.PhotoImage(file="fig/8.png")
    cx, cy =  300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.pack()

    key =  ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyPress>",key_down)
    
    main_proc()
    
    root.mainloop()
    