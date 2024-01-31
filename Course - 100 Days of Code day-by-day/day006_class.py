import turtle

class Car:
    def __init__(self):
        self.direction = "North"
        self.num_of_wheels = 4
        self.amount_of_fuel = 60
        self.position = {"x": 0, "y": 0}

    def move(self, vector):
        self.position["x"] += vector[0]
        self.position["y"] += vector[1]

# Create an instance of the Car class
my_car = Car()
my_car.move([12, 2])
my_car.move([-1, -3])
my_car.position["x"] = 0
print(my_car.position)

# Create a turtle screen
my_screen = turtle.Screen()

# Set the screen dimensions explicitly (adjust these values as needed)
my_screen.setup(width=800, height=600)

# Change the background color of the screen to yellow
my_screen.bgcolor("yellow")

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.forward(100)

# Close the turtle graphics window when clicked
my_screen.exitonclick()

# Keep the window open
turtle.done()