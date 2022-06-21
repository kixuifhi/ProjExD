import tkinter as tk  #インポート
import tkinter.messagebox as tkm
import random

def button_click(event):
    
    btn = event.widget
    num = btn['text'] #クリックされたボタンの文字
    if num == '=':
       eqn = entry.get()
       res = eval(eqn)
       entry.delete(0, tk.END)
       entry.insert(tk.END,res)

    if num == "AC":
       entry.delete(0, tk.END)

    else:
    #tkm.showinfo("",f'{num}のボタンがクリックされました')
       entry.insert(tk.END,num)

if __name__=='__main__':

    root = tk.Tk()  
root.title('電卓')
#root.geometry("300x600")

entry = tk.Entry(root, justify='right', width=10, font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)

r,c=1,0 #r行 c列
for i,num in enumerate([j for j in range(9,-1,-1)]+["+","-","*","/",".","=","AC"]):
   btn = tk.Button(root, 
                   text=f'{num}',
                   width=6,  #ボタンの大きさ
                   height=1,
                   bg=["#"+''.join([random.choice('0123456789abcdef') for j in range(6)])],  #色ランダム
                   fg=["#"+''.join([random.choice('0123456789abcdef') for j in range(6)])],   #ffff00
                   font=('Chiller',30)
                   )
   
   btn.bind("<1>",button_click)
   btn.grid(row=r,column=c)
   c += 1
   if (i+1)%3 == 0:
     r += 1
     c = 0

root.mainloop()

