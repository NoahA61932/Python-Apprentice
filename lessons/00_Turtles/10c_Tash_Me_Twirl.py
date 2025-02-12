
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90
colors = [ 'red', 'blue', 'black', 'orange']

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