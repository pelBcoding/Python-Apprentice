import turtle
import random
turtle.setup(width=600, height=600)
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

mason67 = turtle.Turtle()
mason67.shape("turtle")
mason67.pendown()
mason67.speed(30)
mason67.pensize(10)
for i in range(100000000):
    mason67.left(360 / 3 + 2*5)
    mason67.forward(5*i)
    mason67.pencolor(getRandomColor())
    mason67.fillcolor(getRandomColor())
    mason67.write("u a bum chase")
turtle.exitonclick()
