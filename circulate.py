import turtle as t
color2=['purple','blue','yellow','white']
t.bgcolor("black")
t.speed(0)

for i in range(200):
	for j in color2:
		t.pencolor(j)
		t.forward(i)
		t.left(89) 
