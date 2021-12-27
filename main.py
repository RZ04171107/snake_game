from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

COLLISION_DIS = 15
WALL_COR_POS = 280
WALL_COR_NEG = -280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.north, "w")
screen.onkey(snake.south, "s")
screen.onkey(snake.east, "d")
screen.onkey(snake.west, "a")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < COLLISION_DIS:
        food.refresh()
        snake.extend()
        scoreboard.upgrade_score()

    # Detect collision with wall
    if snake.head.xcor() > WALL_COR_POS or snake.head.xcor() < WALL_COR_NEG or snake.head.ycor() > WALL_COR_POS or snake.head.ycor() < WALL_COR_NEG:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail.
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
