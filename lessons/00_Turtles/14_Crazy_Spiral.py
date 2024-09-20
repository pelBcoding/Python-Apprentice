"""
Crazy Spiral

#Make your own crazy spiral with a pattern like
#in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
import random 
import turtle  # Copy code to make a turtle and set up the window
turtle.setup(width= 600, height= 600)
diddy = turtle.Turtle() # Create a turtle named t
colors = [ 'red', 'blue', 'black', 'orange']
diddy.goto(0,0)
def getNextColor(i):
    return colors[i % len(colors)]
baseSize = 100  # the size of the black part of the star
flameSize = 100
diddy.speed(1000) 
# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def make_a_shape(t):

    diddy.pencolor(getRandomColor())

    diddy.fillcolor(getRandomColor()) 
   
    diddy.begin_fill()

    diddy.forward(64) 

    diddy.left(40) 

    diddy.forward(flameSize) 

    diddy.right(170) 

    diddy.forward(flameSize) 

    diddy.right(62) 

    diddy.forward(baseSize) 

    diddy.end_fill()


# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 57

for i in range(700):
    make_a_shape(turtle)
    diddy.right(360/num_shapes)

    
turtle.exitonclick()
    
