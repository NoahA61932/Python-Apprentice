"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90
colors = [ 'purple', 'grey', 'green', 'red']

for color in colors:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)


forward = 50

for left in [ 45, 60, 90, 45, -90, 60, 22 , -45, 90]:
    print(f"tina.forward({forward})")
    print(f"tina.left({left})")
    print(" ")

forward = 50
left = 90
colors = [ 'red', 'green', 'grey', 'purple']

for color in colors:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)


forward = 50

for left in [ 45, 60, 90, 45, -90, 60, 22 , -45, 90]:
    print(f"tina.forward({forward})")
    print(f"tina.left({left})")
    print(" ")

turtle.done()



# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here

turtle.done()                    # Close the window when we click on it