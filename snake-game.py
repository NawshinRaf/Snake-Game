#!/usr/bin/env python
from turtle import Turtle,Screen
import turtle as t
import time
from Snake import Snake
from Food import Food
from Score import Score




myscreen = Screen()
myscreen.setup(width=500,height=500)
myscreen.bgcolor("black")
myscreen.title("The Snake Game")
myscreen.tracer(0)






#Start the game

game_is_on = True
myscreen.listen()
my_snake = Snake()
myscreen.update()
my_snake.move_snake(myscreen)
food =Food()
score = Score()

while game_is_on:

    myscreen.update()
    time.sleep(0.1)

    my_snake.snake_movement(myscreen)
    #check for collision
    collided =  my_snake.detect_collision(myscreen)

    if collided:
        user_choice = myscreen.textinput("GAME OVER","Want to start over?(y/n)")
        if user_choice =='y':
            myscreen.clear()
            myscreen.setup(width=500, height=500)
            myscreen.bgcolor("black")
            myscreen.title("The Snake Game")
            myscreen.tracer(0)
            myscreen.listen()
            my_snake.move_snake(myscreen)
            my_snake.initialsnake()
            food = Food()
            score = Score()

            continue
        else:
            game_is_on = False
            exit()
            break


    #Check if food is eaten

    food_eaten = my_snake.snake_grow(food.food)

    if food_eaten:
        food.change_position()
        score.update_score()














myscreen.exitonclick()