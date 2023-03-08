# game of life sim using python 

from random import choice
from turtle import *
import turtle
from freegames import square

cells = {}


# 1 init function
def initialize():
    # randomly initialize cells
    for x in range( -200, 200, 10):
        for y in range( -200, 200, 10):
            cells[x,y] = False

    for x in range( -50, 50, 10):
        for y in range( -50, 50, 10):
            cells[x,y] = choice([True, False])


# 2 step function
def step():
    # game creation
    neighbors = {}

    for x in range( -190, 190, 10):
        for y in range( -190, 190, 10):
            count = -cells[x,y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x+h, y+v ]
            neighbors[x,y] = count

        for cell, count in neighbors.items():
            if cells[cell]:
                if count < 2 or count > 3:
                    cells[cell] = False
            elif count == 3:
                cells[cell] = True


# 3 drawing func
def draw():
    # drawing green squares (color can be changed)           
    step()
    clear()
    for (x,y), alive in cells.items():
        color = 'green' if alive else 'black'
        square(x,y,10,color)
    update()
    ontimer(draw, 100)

#  Creating turtle window
turtle.title("Game of life")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
done()
