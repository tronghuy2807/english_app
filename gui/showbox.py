import Tkinter as tk

root = tk.Tk()

v = tk.IntVar()

def close_window():
    root.destroy()
def pass_result():
    print ('xxx',v.get())
    close_window()
def get_text():
    return 'HELLO'

tk.Label(root,
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root,
              text=get_text(),
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root,
              text="Perl",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)

tk.Button(root,text='OK',fg='blue',command=pass_result).pack()

root.mainloop()