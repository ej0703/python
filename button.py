from tkinter import *
from tkinter import messagebox

def myFunc():
	messagebox.showinfo("강아지 버튼","강아지가 귀엽죠?^^")

window=Tk()
'''
button1=Button(window,text="파이썬 종료",fg="red",command=quit)
'''
photo=PhotoImage(file="python__image/gif/dog2.gif")
button1=Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()