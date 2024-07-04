#10 * 10 rows of spots, each dot around 20 in size, spaced apart by 50 spaces
import turtle as turtle_module
import random
#we get the turtle module to change its color mode to 255
turtle_module.colormode(255)
#tim object created
tim=turtle_module.Turtle()
tim.speed("fastest")
#to remove the lines, pen up
tim.penup()
#hiding the turtle
tim.hideturtle()
color_list = [(218, 165, 82), (243, 244, 247), (245, 230, 241), (82, 104, 151), (109, 154, 200), (243, 237, 225), (69, 127, 97), (129, 23, 61), (110, 173, 133), (158, 47, 81), (215, 202, 135), (152, 160, 53), (202, 116, 162), (239, 246, 243), (191, 69, 42), (36, 38, 81), (122, 116, 165), (205, 100, 54), (197, 83, 101), (87, 161, 117)]

#to set the direction from where the dot starts
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

#dot count - rep current num of dots that have been painted
for dot_count in range(1, number_of_dots +1):
    #chooses a random color from the list and then create a dot
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    #after getting the dot count, if statement to check if the dot count %10==0, meaning dot count 10,20,30,,,100
    #under those circumstances we want tim to move so it can go to a new line
    if dot_count % 10 ==0:
        #turn tim to face up - heading of 90 (right), left- 180
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        #move forward by 10 times, 50 paces = 500
        tim.forward(500)
        #facing right again- 0
        tim.setheading(0)


#creating new screen object from turtle module, screen class
screen = turtle_module.Screen()
screen.exitonclick()
