from turtle import Turtle
import random

COLOURS = ["red", "blue", "green", "purple", "pink", "orange", "yellow"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.colour()
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def colour(self):
        random_colour = random.choice(COLOURS)
        self.color(random_colour)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.colour()
        self.goto(random_x, random_y)
