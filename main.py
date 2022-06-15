from turtle import Screen , Turtle
from snake import Snake
from food import Food
import time
from score import Score
import random
is_ps=True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
new_food=Food()
new_score=Score()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
def pause1():
    return









game_is_on = True
game_is_tail=True
while game_is_on and game_is_tail:
    screen.update()
    time.sleep(0.1)

    snake.move()







    game_is_on=snake.is_hit_wall()
    game_is_tail=snake.is_hit_his_tail()

    if snake.head.distance(new_food) < 15:

        new_food.refresh()
        new_score.increase_score()
        snake.increase_snake()
else:
    snake.is_hit_wall()







screen.exitonclick()
