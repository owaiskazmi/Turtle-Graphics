# 🐢 Colorful Turtle Art 🌈

Create mesmerizing geometric art using Python's `turtle` module! Watch as the turtle draws **colorful squares in a circular pattern** for a vibrant visual effect. ✨🎨

## Features ⭐

- 🟦 Draws multiple squares rotated in a circular pattern  
- 🌈 Uses bright colors: cyan, magenta, yellow, lime, orange, red, and blue  
- ⚡ Adjustable speed and pen width  
- 🐢 Fun way to explore Python graphics and loops  

## Requirements 🛠️

- Python 3.x  
- `turtle` module (pre-installed with Python)  

## How to Run ▶️

1. Clone or download this repository  
2. Open the Python file (`turtle_graphics.py`) in your IDE or editor  
3. Run the script:

```bash
python turtle_graphics.py
```
4. Watch the colorful turtle art appear in a new window! 🖼️

### Code Overview 📝
```bash
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
```

### How it Works 🔍

1. 🟩 The turtle draws a square of 150 units
2. 🔄 After each square, the turtle rotates 10° to form a circular pattern
3. 🌈 Colors cycle through a predefined list to create a vibrant effect
4. 36 iterations complete the full circular art 🎨

### Screenshots 📸
[![Turtle Graphics](https://github.com/owaiskazmi/Turtle-Graphics/blob/main/Screenshots/turtle.png)](https://github.com/owaiskazmi/Turtle-Graphics/blob/main/Screenshots/turtle.png)
