from tkinter import *
from tkinter import messagebox
'''
def keyEvent(event):
	messagebox.showinfo("키보드 이벤트","눌린 키 : "+chr(event.keycode))
	print(event.keycode)
'''
def keyEvent(event):
	if event.keycode==37:
		messagebox.showinfo("키보드 이벤트","눌린 키 : shift + 아래쪽 화살표")
	elif event.keycode==38:
		messagebox.showinfo("키보드 이벤트","눌린 키 : shift + 위쪽 화살표")
	elif event.keycode==39:
		messagebox.showinfo("키보드 이벤트","눌린 키 : shift + 오른쪽 화살표")
	elif event.keycode==40:
		messagebox.showinfo("키보드 이벤트","눌린 키 : shift + 왼쪽 화살표")

window=Tk()

window.bind("<Shift-Up>",keyEvent)
window.bind("<Shift-Down>",keyEvent)
window.bind("<Shift-Left>",keyEvent)
window.bind("<Shift-Right>",keyEvent)

window.mainloop()