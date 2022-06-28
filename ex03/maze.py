import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random 



def key_down(event):
    global key
    key = event.keysym #key event
    #print(f"{key}キーが押されました")

def key_up(event):
    global key
    key = "" #空

def main_proc():
    global mx, my, cx, cy
    delta = { #キー：押されたキー、値：移動幅リスト[x,y]
        "":[0,0],
        "Up":[0,-1],  
        "Down":[0,1],
        "Left":[-1,0],
        "Right":[1,0]}
    
    if maze_bg[my+delta[key][1]][mx+delta[key][0]]==0: #移動先が床ならば
            my, mx = my+delta[key][1], mx+delta[key][0]
        
    else:
        pass
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()    #ウインドウ
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, 
                     height=900,
                     bg = "black")
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)   # 1:壁/0:床を表す
    mm.show_maze(canvas, maze_bg)   # canvasにmaze_bgを描く
    r = random.randint(0,9) #0～9のランダムな数字
    tori1 = tk.PhotoImage(file=f"fig/{r}.png") #画像
    mx, my = 1, 1
    cx, cy =  mx*100+50, my*100+50 
    canvas.create_text(cx, cy, text="すたーと", anchor="center",fill="red") #startの追加
    canvas.create_text(13*100+50, 7*100+50, text="ごーる", anchor="center",fill="red") #goalの追加
    canvas.create_image(cx, cy, image=tori1, tag="tori")
    key =  ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    root.after(20000, lambda: root.destroy()) #20秒でウィンドウを閉じる
    main_proc()
    root.mainloop()
    