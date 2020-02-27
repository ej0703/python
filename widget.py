from tkinter import *

btnList=[NONE]*9
fnameList=["froyo.gif","gingerbread.gif","honeycomb.gif","icecream.gif","jellybean.gif","kitkat.gif","lollipop.gif","marshmallow.gif","nougat.gif"]
photoList=[NONE]*9
i,k=0,0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry("210x210")

for i in range(9):
	photoList[i]=PhotoImage(file="python__image/gif/"+fnameList[i])
	btnList[i]=Button(window,image=photoList[i])

for i in range(3):
	for k in range(3):
		btnList[num].place(x=xPos,y=yPos)
		num += 1
		xPos += 70
	xPos=0
	yPos +=70

window.mainloop()