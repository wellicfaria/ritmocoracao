import tkinter as tk
from player_sound import sound as sd
from player_sound import player as pyr




root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python
tk.Label(root,
        text="Escolha uma Historia:",
        justify = tk.LEFT,
        padx = 20).pack()
for hist in sd.getAllHistory():
    tk.Radiobutton(root,
                   text=hist['name_hist'],
                   padx=20,
                   variable=v,
                   value=int(hist['code_hist'])).pack(anchor=tk.W)



def f_b1():
    pyr.playTogetherSound(v.get(),'0')

def f_b2():
    pyr.playTogetherSound(v.get(),'1')

def f_b3():
    pyr.playTogetherSound(v.get(),'2')

def f_b4():
    pyr.playTogetherSound(v.get(),'3')

def f_b5():
    pyr.playTogetherSound(v.get(),'4')

b1 = tk.Button(frame,
                   text="Botao 1",
                   command=f_b1)
b1.pack(side=tk.LEFT)

b2 = tk.Button(frame,
                   text="Botao 2",
                   command=f_b2)
b2.pack(side=tk.LEFT)

b3 = tk.Button(frame,
                   text="Botao 3",
                   command=f_b3)
b3.pack(side=tk.LEFT)

b4 = tk.Button(frame,
                   text="Botao 4",
                   command=f_b4)
b4.pack(side=tk.LEFT)

b5 = tk.Button(frame,
                   text="Botao 5",
                   command=f_b5)
b5.pack(side=tk.LEFT)

root.mainloop()