import tkinter as tk  #インポート


if __name__=='__main__':
    root = tk.Tk()  
root.title('電卓')
root.geometry("300x500")



btn = tk.Button(root, text='9',width=4,height=2,
font=('Times New Roman',30))
#btn.grid(row=0,column=0)
btn.pack()


root.mainloop()

