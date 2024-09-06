"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
tina.begin_fill()
tina.color("orange")
tina.pendown()
tina.goto(0,0)
tina.forward(60)
for i in range(3):
    tina.right(120)
    tina.forward(120)
tina.end_fill()

tina.goto(0,-20)
tina.color("blue")
tina.begin_fill()
tina.circle(100)
tina.end_fill()

tina.goto(5,30)
tina.color("yellow")
tina.begin_fill()
tina.circle(30)
tina.end_fill()
tina.penup()

tina.goto(-5,100)
tina.begin_fill()
tina.circle(20)
tina.end_fill()

tina.goto(50,80)
tina.begin_fill()
tina.color("red")
tina.circle(25)
tina.penup()
tina.goto(0,0)
tina.end_fill()

tina.goto(-50,30)
tina.color("green")
tina.begin_fill()
tina.circle(15)
tina.end_fill()

tina.goto(0,0)
tina.goto(-50,45)

turtle.exitonclick() 
                   # Close the window when we click on it


# Dont forget to check in your code!