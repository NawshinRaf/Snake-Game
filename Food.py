from turtle import Turtle,Screen
import random


class Food():
    def __init__(self):
        self.food = Turtle("circle")
        self.food.color("white")
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.speed("fastest")
        self.food.penup()


    def change_position(self):
        #get a random x and y coordinate
        random_xcor = random.randint(-230,230)
        random_ycor = random.randint(-230,230)
        self.food.goto(random_xcor,random_ycor)

    def food_position(self):
        return self.food.xcor(),self.food.ycor()





