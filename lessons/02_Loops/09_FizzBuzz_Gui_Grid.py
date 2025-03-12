"""Fizzbuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
our you can convert the number to a string and iterate over the digits

"""
from guizero import App, Box, Text

app = App("Numbers Grid", layout="grid")

# Create a 10x10 grid using nested loops
# Or you can use a single loop and calculate the row and column
 # Change only this line
    # Don't change anything below this line

# In the loop, calculate or increment the number

# Use % determing the display, using fizzbuzz rules

# If you are displaying a number, calculate the sum of the digits and determine the color

# Call Text(app, text='...', grid=[col, row], color=...) to display something. 



# This program is different because we didn't create a turtle first. The
# command here are for the "default turtle"

import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()

baseSize = 150  # the size of the black part of the star
flameSize = 80  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2) 
t.speed(0)  


for i in range(25):

    t.pencolor(getRandomColor())
    t.fillcolor(getRandomColor())  

    t.begin_fill()

    t.right(360 / 8) 
    t.forward(64)

    t.left(40) 

    t.forward(flameSize)
    t.right(170) 
    t.forward(flameSize)
    t.right(62) 
    t.forward(baseSize) 

    t.end_fill()

t.speed(2)  

t.right(90)

import time
print("Start")
time.sleep(5)  # Wait for 5 seconds
print("End")

t.circle(150)
t.begin_fill()

t.hideturtle() # Hide yourturtle so you can see the pattern.

turtle.exitonclick()