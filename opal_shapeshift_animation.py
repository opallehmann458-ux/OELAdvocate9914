import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle for the main character
opal = turtle.Turtle()
opal.shape("circle")
opal.color("orange")
opal.speed(5)

# Bouncing function

def bounce():
    for _ in range(50):
        opal.sety(opal.ycor() + 10)
        screen.update()
        opal.sety(opal.ycor() - 10)
        screen.update()

# Fluttering function

def flutter():
    for _ in range(36):
        opal.right(10)
        screen.update()

# Shape-shifting function

def shape_shift():
    for shape in ["circle", "square", "triangle"]:
        opal.shape(shape)
        screen.update()
        turtle.time.sleep(0.5)

# Main animation loop
while True:
    bounce()
    flutter()
    shape_shift()

# Keep the window open until clicked
screen.mainloop()