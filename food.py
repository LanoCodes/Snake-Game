from turtle import Turtle
from turtle import Screen
import random as r
import random



class Food(Turtle):

    def __init__(self):
      super().__init__()
      self.shape("circle")
      self.penup()
      self.shapesize(stretch_len=0.5, stretch_wid=0.5)
      Screen().colormode(255)
      # self.color(COLOR)
      self.set_color()
      self.speed("fastest")
      self.refresh()

    def set_color(self):
      color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
      self.color(color)

    def refresh(self):
      self.set_color()
      random_x = random.randint(-280, 280)
      random_y = random.randint(-280, 280)
      self.goto(random_x, random_y)