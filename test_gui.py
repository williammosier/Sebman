import tkinter as tk
from tkinter import messagebox

HEIGHT = 600
WIDTH = 800

def output():
	print("sample output")

def check():
	print(CheckVar1.get())

def entryfunc(entry):
	print('this is the entry:', entry)

def areYouSure():
	print(messagebox.askokcancel("are you sure?","deleting a person is perminent"))

root = tk.Tk()
root.title("Sebman")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(frame, text='button', command=lambda: entryfunc(entry.get()))
button.place(x=0, y=0)

button2 = tk.Button(frame, text='delete person', command=areYouSure)
button2.place(x=100, y=80)

CheckVar1 = tk.IntVar()
checkbutton = tk.Checkbutton(frame, text = "checkbutton", variable = CheckVar1, onvalue = 1, offvalue = 0, command=check)
checkbutton.place(x=50, y=50)

entry = tk.Entry(frame)
entry.place(x=100, y=0)

label = tk.Label(frame, text='label')
label.place(x=250, y=0)

listbox = tk.Listbox(frame, selectmode='SINGLE')
listbox.insert(1, "item 1")
listbox.insert(2, "item 2")
listbox.insert(3, "item 3")
listbox.insert(4, "item 4")
listbox.place(x=300, y=0)

menubutton = tk.Menubutton(frame, text='menubutton')
menubutton.place(x=500, y=0)

menu = tk.Menu(root)
submenu = tk.Menu(menu, tearoff=0)
submenu.add_command(label="one", command=output)
submenu.add_command(label="two", command=output)
submenu.add_command(label="three", command=output)
menu.add_cascade(label="file", menu=submenu)

message = tk.Message(frame, text='message, message, message')
message.place(x=600, y=0)

radiobutton = tk.Radiobutton(frame)
radiobutton.place(x=700, y=0)

scale = tk.Scale(frame)
scale.place(x=0, y=100)

#start of scrollbar test
scrollframe = tk.Frame(root)
scrollframe.place(x=200, y=200, width=150, height=100)

scrollbar = tk.Scrollbar(scrollframe)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(scrollframe, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(tk.END, "This is line number " + str(line))

mylist.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config( command = mylist.yview )
#end of scrollbar test

spinbox = tk.Spinbox(frame, from_=0, to=100)
spinbox.place(x=400, y=200)

root.config(menu=menu)
root.mainloop()