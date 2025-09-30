import turtle

scale = 10
#any numbers
em = 1.5
#1.5 for best results, any for goofy results
#1.4 and 1.6 work good to.

mid_x = -6*scale

def curve(f, r):
    for i in range(4):
        turtle.forward(f)
        turtle.right(r)
    turtle.right(15)

def ear_in(f):
    turtle.forward(f)
    turtle.left(120)
    turtle.forward(f-(scale*0.5))
    turtle.left(100)
    turtle.forward(f-(scale*.15))
    turtle.left(120)

turtle.speed(26)

def cheek_fuz():
    for i in range (2):
        turtle.forward(scale*3)
        turtle.right(90)
        turtle.forward(scale*3)
        turtle.left(90)

def draw_face_inside_curves():
    turtle.goto(-scale*12.5, scale*8.5)
    turtle.down()
    turtle.left(22)
    curve(scale*2.03, 5.9)
    turtle.up()
    turtle.goto(-scale*0.1, scale*8.5)
    turtle.down()
    turtle.right(91.4)
    curve(scale*1.73, -6)

def draw_eyes():
    dist_nose_eyes = 4*scale
    for i in range(-1, 2, 2):
        turtle.goto(mid_x + i*dist_nose_eyes, scale*5)
        turtle.dot(scale*.9)

def mouth_draw():
    turtle.goto(-scale*5.56, scale*4.35)
    turtle.left(61)
    turtle.down()
    turtle.forward(scale*2)
    turtle.up()
    turtle.goto(-scale*4, scale*2.5)
    turtle.right(80)
    turtle.down()
    curve(scale, 10)


#bottom of face 
turtle.left(195)
curve(scale*3, 10)
#l cheek
cheek_fuz()
#l top face
turtle.right(50)
turtle.forward(scale*8)
turtle.right(130)
turtle.forward(scale*3)
turtle.left(50)
#crown of head 
curve(scale*2, 7)
#r top face
turtle.left(80)
turtle.forward(scale*3)
turtle.right(136)
turtle.forward(scale*8+2)
turtle.left(45)

#r cheek
cheek_fuz()
turtle.up()
#face inside curves
draw_face_inside_curves()
turtle.up()
#nose dash
turtle.goto(-scale*5.15,scale*4.8)
turtle.right(35)
turtle.down()
turtle.forward(scale*0.9)
turtle.up()
#ear inside start
turtle.goto(-scale*12.3, scale*16)
turtle.left(90)
turtle.down()
ear_in(scale*em)
turtle.up()
turtle.goto(-scale*0.4, scale*16)
turtle.right(21)
turtle.down()
ear_in(scale*em)
turtle.up()

draw_eyes()
mouth_draw()

turtle.up()
turtle.goto(scale*10, -scale*10)

turtle.exitonclick()
