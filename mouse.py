from tkinter import *
from tkinter import messagebox

def clicked(event):
	if event.num==1:
		messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨")
	elif event.num==3:
		messagebox.showinfo("마우스","마우스 오른쪽 버튼이 클릭됨")

window=Tk()

window.bind("<Button-1>",clicked)
window.bind("<Button-3>",clicked)

window.mainloop()