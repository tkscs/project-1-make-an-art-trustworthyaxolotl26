import turtle

scale = 20
#only 10 for now

def curve(f, r):
    for i in range(4):
        turtle.forward(f)
        turtle.right(r)
    turtle.right(15)

def earI(f):
#1.5 for best results, any for goofy results
    turtle.forward(f)
    turtle.left(120)
    turtle.forward(f-5)
    turtle.left(100)
    turtle.forward(f-1.5)
    turtle.left(120)

turtle.speed(2)

def draw_face_inside_curves():
    turtle.goto(-scale*12.5, scale*8.5)
    turtle.down()
    turtle.left(22)
    curve(scale*2.03, 5)
    turtle.up()
    turtle.goto(-scale*0.1, scale*8.5)
    turtle.down()
    turtle.right(92)
    curve(scale*1.75, -5)
    print(turtle.position())

turtle.left(195)
print(turtle.heading())
curve(scale*3, 10)
print(turtle.heading())
for i in range (2):
    turtle.forward(scale*3)
    print(turtle.position())
    turtle.right(90)
    turtle.forward(scale*3)
    turtle.left(90)

turtle.right(50)
turtle.forward(scale*8)
turtle.right(130)
turtle.forward(scale*3)
turtle.left(50)
curve(scale*2, 7)
turtle.left(80)
turtle.forward(scale*3)
turtle.right(136)
turtle.forward(scale*8+2)
turtle.left(45)
for i in range (2):
    turtle.forward(scale*3)
    print(turtle.position())
    turtle.right(90)
    turtle.forward(scale*3)
    turtle.left(90)
turtle.up()
#face inside curves
draw_face_inside_curves()
turtle.up()
#nose dash
turtle.goto(-scale*5,scale*4.8)
turtle.right(35)
turtle.down()
turtle.forward(scale*1.2)
turtle.up()
turtle.goto(-scale*12.3, scale*16)
turtle.left(90)
turtle.down()
earI(scale*1.5)
turtle.up()
turtle.goto(-scale*0.4, scale*16)
turtle.right(21)
turtle.down()
earI(scale*1.5)
turtle.up()
turtle.goto(-scale*2, scale*5)
turtle.dot()
turtle.goto(-scale*10, scale*5)
turtle.dot()
turtle.goto(-scale*5.5, scale*4.2)
turtle.left(61)
turtle.down()
turtle.forward(scale*2)
turtle.up()
turtle.goto(-scale*4, scale*2.5)
turtle.right(80)
turtle.down()
curve(scale, 10)
turtle.up()
turtle.goto(scale*10, -scale*10)

turtle.exitonclick()