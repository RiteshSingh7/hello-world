import turtle
wn = turtle.Screen()
bcolor = input('Enter background colour : ')
wn.bgcolor(bcolor)

tess = turtle.Turtle()
col = input('Enter pen colour : ')
tess.color(col)
width = input('Enter pen width : ')
tess.pensize(int(width))

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()