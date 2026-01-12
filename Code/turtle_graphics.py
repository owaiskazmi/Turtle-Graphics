import turtle

screen = turtle.Screen ()
screen.bgcolor ("black")
screen.title ("Colorful Turtle Art")

t = turtle.Turtle ()
t.speed (3)              
t.width (3)
t.hideturtle ()

colors = ["cyan", "magenta", "yellow", "lime", "orange", "red", "blue"]

for i in range (0, 36):
    t.color (colors [i % len (colors)])
    for j in range (0, 4):
        t.forward (150)
        t.right (90)
    t.right (10)

turtle.done ()
