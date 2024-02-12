from turtle import Turtle, Screen
import random
import math

all_turtles = []
main_distance = 45

def position_refinement (given_number, distance = main_distance):
    if given_number != 0 :
      return int(  (given_number+(distance*0.5)*abs(given_number)/given_number)/(distance)  ) * (distance)
    else:
        return given_number


def create_random_turtle(x,y):
    new_turtle = Turtle()
    # new_turtle.shape(random.choice(["arrow", "turtle", "circle", "square", "triangle", "classic"]))
    new_turtle.shape("turtle")
    new_turtle.color(random.choice(["red", "blue", "green", "orange", "purple"]))
    all_turtles.append(new_turtle)
    # new_turtle.penup()

    # solution 1:
    # new_turtle.setpos(x,y)

    # solution 2:
    new_turtle.goto(x, y)

    # solution 3:
    # new_turtle.setx(x)
    # new_turtle.sety(y)


    # new_turtle.pendown()
    return new_turtle

def check_collision(x, y, turtles):
    for turtle in turtles:
        distance = turtle.distance(x, y)
        if distance < main_distance/2 + 1  : 
            return True
    return False

def on_click(x, y):
    x = position_refinement(x)
    y = position_refinement(y)
    if not check_collision(x, y, all_turtles):
        create_random_turtle(x,y)
    else:
        print ("there is a collision")
        remove_turtle(find_turtle(x,y))

def remove_turtle(turtle):
    turtle.clear()
    all_turtles.remove(turtle)
    print ("the extra turtle is removed")

def find_turtle(x, y, turtles = all_turtles):
    for turtle in turtles:
        if turtle.xcor() == x and turtle.ycor() == y:
            print ("we find the turtle")
            turtle.color("white")
            return turtle
    return None

def move_turtle(turtle, x_offset, y_offset):
    turtle.goto(turtle.xcor() + x_offset, turtle.ycor() + y_offset)

screen = Screen()
screen.setup(width=850, height=650)
screen.bgcolor("white")

for i in range(0,40,int(main_distance)):
    for j in range(0,60,int(main_distance)):
        on_click(i,j)


my_turtle = all_turtles[0]
# my_turtle.begin_fill()
# while True:
#     my_turtle.forward(200)
#     my_turtle.left(170)
#     my_turtle.stamp()
#     if abs(my_turtle.pos()) < 1:
#         break
# my_turtle.end_fill()

screen.onscreenclick(on_click)

def polygon_drawer(given_turtle):
    my_turtle = given_turtle
    n = int(input("tell me know the n: ")) # Most complicated shape
    my_turtle.setpos(-50,150)

    for n_polygon in range(n, 2, -1) :
        print(f"we are going to draw polygon({n_polygon})")
        angle = (n_polygon-2)* 180 / n_polygon
        print(f"anglie is: {angle}")
        rnadom_colo_1 = random.choice(["red", "blue", "green", "orange", "purple"])
        rnadom_colo_2 = random.choice(["red", "blue", "green", "orange", "purple"])
        my_turtle.color(rnadom_colo_1,rnadom_colo_2)
        my_turtle.begin_fill()
        for turn in range(0,n_polygon,1):
            print(str(turn))
            my_turtle.forward(100)
            my_turtle.right(180-angle)
        my_turtle.end_fill()


angle_holder = 0
x_holder = 0
y_holder = 0
my_turtle.setpos(x_holder,y_holder)
# angle = int(input("give me the angle: "))
# my_turtle.right(angle)

def where_to_meet_borders (the_x,the_y,the_angle):

    x_border = the_x
    y_border = the_y
    return_angle = the_angle * -1
    default_screen_width = 800
    default_screen_height = 600

    while the_angle > 180 :
        the_angle = the_angle - 360

    while the_angle < -180 :
        the_angle = the_angle + 360

    if -90 < the_angle and the_angle < 90 :
        extreme_x = default_screen_width * 0.5
    elif (90 < the_angle and the_angle < 180 ) or (-180 < the_angle and the_angle < -90) :
        extreme_x = default_screen_width * -0.5

    if 0 < the_angle  and the_angle < 180 :
        extreme_y = default_screen_height * 0.5
    elif  -180 < the_angle  and the_angle < 0 :
        extreme_y = default_screen_height * -0.5   
    
    if the_angle == 0 :
        extreme_x = default_screen_width * 0.5
        extreme_y = the_y
        return_angle = 180

    if the_angle == 90 :
        extreme_x = the_x
        extreme_y = default_screen_height * 0.5
        return_angle = -90

    if the_angle == 180 or the_angle == -180 :
        extreme_x = default_screen_width * -0.5
        extreme_y = the_y
        return_angle = 0

    if the_angle == -90 :
        extreme_x = the_x
        extreme_y = default_screen_height * -0.5
        return_angle = 90

    x_border = extreme_x
    y_border = extreme_y
    # xy_border calculator:
        
    angle_in_rad = the_angle * math.pi/180
    x_lengh = abs( extreme_x - the_x)
    y_lengh = x_lengh * abs(math.tan(angle_in_rad))
    

    if (0 < the_angle and the_angle < 180) and the_angle != 90 :

        if y_lengh + the_y < default_screen_height * 0.5:
            x_border = extreme_x
            y_border = y_lengh + the_y
            return_angle = 180 - the_angle
        else :
            x_border = abs(extreme_y - the_y)/math.tan(angle_in_rad) + the_x
            y_border = extreme_y

            

    elif  (-180 < the_angle  and the_angle < 0) and the_angle != -90:

        if abs (the_y - y_lengh) < default_screen_height * 0.5:
            x_border = extreme_x
            y_border = the_y - y_lengh
            return_angle = 180 - the_angle
        else: 
            x_border = (extreme_y - the_y)/math.tan(angle_in_rad) + the_x
            y_border = extreme_y
    
    return (x_border, y_border, return_angle)


def random_position() :
    x = (random.randint(-400, 400),random.randint(-300, 300))
    print (x)
    return x

my_turtle.penup()
for _ in range(0,5):
    new_pos = random_position()
    x = new_pos[0]
    y = new_pos[1]
    # x = 51
    # y = -100
    my_turtle.goto(x,y)
    my_angle = -45
    my_turtle.pendown() 
    place_to_go = where_to_meet_borders(x,y,my_angle)
    my_turtle.goto(place_to_go[0], place_to_go[1])
    my_turtle.stamp()

    for _ in range(0,3):
        new_pos = my_turtle.pos()
        x = new_pos[0]
        y = new_pos[1]
        place_to_go = where_to_meet_borders(x,y,place_to_go[2])
        my_turtle.goto(place_to_go[0], place_to_go[1])
        my_turtle.stamp()

    my_turtle.penup()



screen.mainloop()
