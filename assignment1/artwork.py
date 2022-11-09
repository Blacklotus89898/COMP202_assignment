# name: Steve Chen
# Id: 261106847

import turtle
#pen.speed("fastest")

def move(x,y):
    """(int, int) -> position
    Lifts the pen up to the x and y position and puts the pen down
    """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def cross(l): 
    """(int)-> shape
    Draws a cross with equal line length of l
    """
    for i in range(4):
        for j in range (3):
            turtle.rt(90)
            turtle.forward(l)
        turtle.lt(180)

def s_letter(r,a):
    """(int, int) -> letter
    Draws the letter S with 2 arcs of radius r and angle a
    """
    turtle.circle(r, a)
    turtle.lt(180)
    turtle.circle(r, -a)

def star(n, l):
    """ (int, int) -> shape 
    Creates a shape with n sides of length l
    """
    a = 360/n
    for i in range(int(n)):
        turtle.forward(l)
        turtle.rt(a)
        turtle.forward(l)
        turtle.lt(2*a)

def flower(r, n): 
    """(int, int) -> shape
    Draws a flower pattern with n sides using curves of radius r in degrees
    """
    for i in range (n):
        turtle.circle(r, 360/n)
        turtle.lt(360/n)

def petal(r,n):
    """(int, int)-> shape
    Draws n petals with a curvature of r degrees
    """
    for i in range (n):
        turtle.circle(r, 360/n)
        turtle.lt(180-720/(2*n))
        turtle.circle(r, 360/n)
        turtle.lt(360 -(180-720/(2*n)) - 720/n) 
        turtle.lt(-360/n)


def my_artwork():
    s_letter(20, 270)
    move(100, 100)
    petal(100, 6)
    turtle.color("green")
    petal(150, 3)
    move(200,-100)
    turtle.color("red")
    flower(100,5)
    move(150, 150)
    flower(60,3)
    move(-100, 200)
    cross(80)
    turtle.color("blue")
    move(-100, -200)
    star(7, 20)
    turtle.color("violet")
    move(-150, -150)
    star(5, 30)
