import turtle

st = 80

def curve(f, r):
    for i in range(4):
        turtle.forward(f)
        turtle.right(r)
    turtle.right(15)

turtle.speed(15)

turtle.left(195)
curve(30, 10)
for i in range (2):
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
turtle.right(50)
turtle.forward(st)
turtle.right(130)
turtle.forward(30)
turtle.left(50)
curve(20, 7)
# turtle.right(50)




turtle.exitonclick()