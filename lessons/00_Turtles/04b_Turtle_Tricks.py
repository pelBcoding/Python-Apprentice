"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.penup()
tina.goto(0,110)
tina.speed(3)
tina.pensize(width= 20)
tina.pencolor("green")
tina.pendown()
tina.right(72)
tina.forward(100)

tina.pencolor("yellow")
tina.right(72)
tina.forward(100)

tina.pencolor("blue")
tina.right(72)
tina.forward(100)

tina.pencolor("red")
tina.right(72)
tina.forward(100)

tina.pencolor("orange")
tina.right(72)
tina.forward(100)
tina.penup

turtle.exitonclick()                    # Close the window when we click on it
