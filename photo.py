from tkinter import *
window=Tk()
'''
photo=PhotoImage(file="python__image/gif/dog.gif")
label1=Label(window, image=photo)

label1.pack()
'''
photo1=PhotoImage(file="python__image/gif/cat.gif")
label1=Label(window, image=photo1)
photo2=PhotoImage(file="python__image/gif/cat2.gif")
label2=Label(window, image=photo2 )

label1.pack(side=LEFT)
label2.pack(side=LEFT)
window.mainloop()