from turtle import Turtle, Screen
from snake import *
from food import *
import time

turtle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to Snake")
screen.tracer(0)
# The 0 argument in tracer sets the screen update to off


# Snake body creates itself by calling create function in init
snake1 = Snake()
food = Food()

# Moving the snake by using event listeners()
screen.listen()
screen.onkey(snake1.up,'Up')
screen.onkey(snake1.down,'Down')
screen.onkey(snake1.left,'Left')
screen.onkey(snake1.right,'Right')

game_is_on = True
score = 0

while game_is_on:

    screen.update()
    # Update the screen only AFTER all body parts of snake have moved ahead by 20 paces forward
    time.sleep(0.07)
    snake1.move()

    # Detect collision with food using distance method in class turtle
    if snake1.head.distance(food) < 15:
        food.new_food_loc()
        snake1.create_snake()
        score += 1
        turtle.color('white')
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition(0, 250)
        turtle.clear()
        turtle.write(f"Score = {score}", align='center', font=('Arial', 20, 'normal'))

        # You need to use clear otherwise scores will overlap with each other

    # Detect collision with wall
    if (snake1.head.xcor() < -280
        or snake1.head.xcor() > 280
        or snake1.head.ycor() > 280
        or snake1.head.ycor() < -280):
        turtle.setposition(0, 0)
        turtle.write(f"GAME OVER", align='center', font=('Arial', 20, 'normal'))
        game_is_on = False

    # Detect collision with its own tail
    for snake_part in snake1.snake_body[1:]:  # Starts from pos 1. Otherwise it will check distance of snake head from snake head itself
        if snake1.head.distance(snake_part) < 10:
            turtle.setposition(0, 0)
            turtle.write(f"GAME OVER", align='center', font=('Arial', 20, 'normal'))
            game_is_on = False


screen.exitonclick()
