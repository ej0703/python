from tkinter import *

window=Tk()
'''
button1=Button(window, text="버튼1")
button2=Button(window, text="버튼2")
button3=Button(window, text="버튼3")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
'''
btnList=[NONE]*3

for i in range(3):
	btnList[i]=Button(window, text="버튼"+str(i+1))

for btn in btnList:
	btn.pack(side=TOP, fill=X,padx=10,pady=10)

window.mainloop()