import turtle as t
'''
t.pensize(10)
t.color("blue")
t.circle(50)

t.penup()
t.goto(50,-50)
t.pendown()
t.color("yellow")
t.circle(50)

t.penup()
t.goto(100,0)
t.pendown()
t.color("black")
t.circle(50)

t.penup()
t.goto(150,-50)
t.pendown()
t.color("green")
t.circle(50)

t.penup()
t.goto(200,0)
t.pendown()
t.color("red")
t.circle(50)
'''
t.pensize(10)
XYC=[(0,0,"blue"),(50,-50,"yellow"),(100,0,"black"),(150,-50,"green"),(200,0,"red")]
for i,j,k in XYC:
	t.penup()
	t.goto(i,j)
	t.pendown()
	t.color(k)
	t.circle(50)