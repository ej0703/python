from tkinter import *
from tkinter import messagebox

def clicked():
	if var.get()==1:
		label1.configure(image=photo1)
	elif var.get()==2:
		label1.configure(image=photo2)
	else:
		label1.configure(image=photo3)

window = Tk()

window.title("2번")
window.geometry("400x400")

'''
animal=[("강아지", 1), ("고양이", 2), ("토끼", 3)]
var = IntVar()

for menu, value in animal:
	Radiobutton(window, text=menu, value=value, variable=var).pack(anchor=W)
	if var.get==1:
		num==1
'''
var = IntVar()
r1=Radiobutton(window, text="강아지", value=1, variable=var)
r2=Radiobutton(window, text="고양이", value=2, variable=var)
r3=Radiobutton(window, text="토끼", value=3, variable=var)
r1.pack()
r2.pack()
r3.pack()

photo1=PhotoImage(file="python__image/gif/dog.gif")
photo2=PhotoImage(file="python__image/gif/cat2.gif")
photo3=PhotoImage(file="python__image/gif/rabbit.gif")
label1=Label(window, image=photo1)

button=Button(window, text="사진 보기", command=clicked)
button.pack()

label1.pack()

photo2=PhotoImage(file="python__image/gif/cat2.gif")
label2=Label(window, image=photo2)
label2.pack()

window.mainloop()