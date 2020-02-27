from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

def func_open():
	filename=askopenfilename(parent=window, filetypes=(("GIF파일","*gif"),("모든 파일","*.*")))
	global photo
	photo=PhotoImage(file=filename)
	pLabel.configure(image=photo)
	pLabel.image=photo

def func_exit():
	window.quit()
	window.destroy()

def func_zoom():
	value=askinteger("값 입력","몇 배 확대?")
	global photo
	photo=photo.zoom(value,value)
	pLabel.configure(image=photo)
	pLabel.image=photo

def func_subsample():
	value=askinteger("값 입력","몇 배 축소?")
	global photo
	photo=photo.subsample(value,value)
	pLabel.configure(image=photo)
	pLabel.image=photo

window=Tk()
window.geometry("400x400")

window.title("명화 감상하기")
'''
label1=Label(window,text="선택된 파일 이름")
label1.pack()
'''
'''
filename=askopenfilename(parent=window, filetypes=(("GIF파일","*gif"),("모든 파일","*.*")))

label1.configure(text=str(filename))
'''
'''
saveFp=asksaveasfile(parent=window, mode="w",defaultextension=".jpg", filetypes=(("JPG파일","*.jpg;*.jpeg"),("모든 파일","*.*")))
label1.configure(text=saveFp)
saveFp.close()
'''
photo=PhotoImage()
pLabel=Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="파일 열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료",command=func_exit)

effectMenu=Menu(mainMenu)
mainMenu.add_cascade(label="이미지 효과",menu=effectMenu)
effectMenu.add_command(label="확대하기",command=func_zoom)
effectMenu.add_command(label="축소하기",command=func_subsample)

window.mainloop()