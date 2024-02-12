from turtle import Turtle, Screen
import random
import math

# Set up the screen
screen = Screen()
screen.setup(width=850, height=650)

# Create a turtle
turtle = Turtle()
turtle.speed("fastest")
# turtle.penup()
turtle.goto(0, 0)
turtle.setheading(random.uniform(0, 360))  # Set a random initial heading

# Function to check if turtle hits screen borders
def check_border_collision(turtle):
    x, y = turtle.position()
    angle = turtle.heading()

    # Check if turtle hits left or right border
    if not (-screen.window_width() / 2 < x < screen.window_width() / 2):
        print(f"Turtle collided with {'left' if x < 0 else 'right'} border at position ({x}, {y}) with angle {angle}")
        angle = 180 - angle  # Reflect angle

    # Check if turtle hits top or bottom border
    if not (-screen.window_height() / 2 < y < screen.window_height() / 2):
        print(f"Turtle collided with {'bottom' if y < 0 else 'top'} border at position ({x}, {y}) with angle {angle}")
        angle = -angle  # Reflect angle

    turtle.setheading(angle)  # Update turtle's angle

# Function to move the turtle forward
def move():
    turtle.forward(45)  # Move turtle forward
    check_border_collision(turtle)  # Check for border collision

# Bind the move function to the "space" key
screen.onkeypress(move, "space")
screen.listen()

# Keep the window open until it is closed manually
screen.mainloop()
