import turtle
import time
import random

delay = 0.1

#Screen
screen = turtle.Screen()
screen.title("SnakeGame by: John Ivan Galang")
screen.bgcolor("black")
screen.setup(width = 700, height = 600)
screen.tracer(0)

#Snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0, 100)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.hideturtle()
snake_head.goto(0, 250)


#Key Bindings
def up_funtion():
	if snake.direction != "down":
		snake.direction = "up"


def down_function():
	if snake.direction != "up":
		snake.direction = "down"


def left_function():
	if snake.direction != "right":
		snake.direction = "left"


def right_function():
	if snake.direction != "left":
		snake.direction = "right"


def move_function():
	if snake.direction == "up":
		y = snake.ycor()
		snake.sety(y + 20)
	if snake.direction == "down":
		y = snake.ycor()
		snake.sety(y - 20)
	if snake.direction == "left":
		x = snake.xcor()
		snake.setx(x - 20)
	if snake.direction == "right":
		x = snake.xcor()
		snake.setx(x + 20)


#Keyboard Bindings
screen.listen()
screen.onkeypress(up_funtion, "w")
screen.onkeypress(down_function, "s")
screen.onkeypress(left_function, "a")
screen.onkeypress(right_function, "d")

#Growth Storage
segments = [] #list
false = True# #boolean value

#Main Loop
while false:
	screen.update()
    
	if snake.xcor() > 320 or snake.xcor() < -320 or snake.ycor() > 290 or snake.ycor() < -290:
		time.sleep(0.3)
		snake.goto(0, 0)
		snake.direction = "Stop"

		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		adds_on = 0
		delay = 0.1
		snake_head.clear()

	if snake.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		#Sub Growth
        #Tail
		sub_growth = turtle.Turtle()
		sub_growth.speed(0)
		sub_growth.shape("square")
		sub_growth.color("green")
		sub_growth.penup()
		segments.append(sub_growth)
		delay -= 0.001

    #Body Collision
	for body_collision in range(len(segments)-1, 0, -1):
		x = segments[body_collision-1].xcor()
		y = segments[body_collision-1].ycor()
		segments[body_collision].goto(x, y)

	if len(segments) > 0:
		x = snake.xcor()
		y = snake.ycor()
		segments[0].goto(x, y)
        

	move_function()#Start

	for segment in segments:
		if segment.distance(snake) < 20:
			time.sleep(1)
			snake.goto(0, 0)
			snake.direction = "stop"
			for segment in segments:
				segment.goto(1000, 1000)
			segment.clear()
			delay = 0.1
			snake_head.clear()

	time.sleep(delay)

#Mainloop of the program
screen.mainloop()
