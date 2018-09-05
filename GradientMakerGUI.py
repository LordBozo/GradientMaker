##Special thanks to ThePhisics101 for helping fix some buttons on the GUI

from tkinter import *
from turtle import *
from tkinter.colorchooser import *
import functools
import math

panel = Tk()
selectionShape = IntVar()
colorMatrix = []
colorC = 0
for x in range(150):
    colorMatrix += [[0, 0, 0]]

def btn_click():
    get_shape()

colormode(255)
tracer(1000)


class DrawClass(object):
    def __init__(self):  ## Initialize global variables
        global cursor
        global startLength
        cursor = Turtle()
        startLength = screensize()[1]
        cursor.width(12)

    def change(self, C1, C2, i,
               Fade):  ##This calculates the difference between the colors that its going between, and finds out how much it needs to change each time
        distance = startLength / Fade
        red = int(C1[0] + ((C2[0] - C1[0]) / distance) * i)
        green = int(C1[1] + ((C2[1] - C1[1]) / distance) * i)
        blue = int(C1[2] + ((C2[2] - C1[2]) / distance) * i)
        cursor.color((red, green, blue))

    def move(self, x, y):  ##moves the turtle somewhere without leaving a line
        cursor.up()
        cursor.goto(x, y)
        cursor.down()

    def Circle(self, radius,
               degree):  ## Custom Circle function cuz Turtle's default one is really slow and poorly optimized for smaller sizes
        cursor.down()
        mult = radius / abs(radius)
        for x in range(int(degree / 2)):
            cursor.left(mult)
            cursor.forward((2 * math.pi * radius) / 360)
            cursor.left(mult)

    ################################################################################
    ######                     Shape Definitions                               #####
    ################################################################################

    def flower(self, Fade, Colors):
        self.move(-startLength / 2, startLength / 2)
        cursor.setheading(0)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.forward(startLength - (startLength / Fade) * x - i)
                cursor.right(105)
        update()
        reset()

    def circle1(self, Fade, Colors):
        self.move(0, 0)
        cursor.pensize(4)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                self.Circle(startLength, 180)
                self.Circle(-startLength, 180)
                cursor.right(360 / startLength)
        update()
        reset()

    def circle2(self, Fade, Colors):
        cursor.left(90)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.dot(startLength - (startLength / Fade) * x - i)
                cursor.forward(1 / (10 * startLength))
        update()
        reset()

    def polygon(self, Fade, Colors):
        print("How many sides do you want on your polygon?")
        Point = int(input())
        cursor.up()
        cursor.goto(math.cos(0), math.sin(0))
        cursor.begin_poly()
        for p in range(Point):
            cursor.goto(math.cos(math.radians(360 / Point) * p), math.sin(math.radians(360 / Point) * p))
        cursor.end_poly()
        register_shape("Polygon", cursor.get_poly())
        cursor.down()
        cursor.shape("Polygon")
        cursor.setheading(90)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.shapesize(startLength - (startLength / Fade) * x - i)
                cursor.stamp()
        update()
        reset()

    def polygonswirl(self, Fade, Colors):
        print("How many sides do you want on your polygon?")
        Point = int(input())
        print("How many degrees do you want to rotate each time?")
        Rotate = float(input())
        cursor.up()
        cursor.goto(math.cos(0), math.sin(0))
        cursor.begin_poly()
        for p in range(Point):
            cursor.goto(math.cos(math.radians(360 / Point) * p), math.sin(math.radians(360 / Point) * p))
        cursor.end_poly()
        register_shape("Polygon", cursor.get_poly())
        cursor.down()
        cursor.shape("Polygon")
        cursor.setheading(90)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.shapesize(startLength - (startLength / Fade) * x - i)
                cursor.stamp()
                cursor.right(Rotate)
        update()
        reset()

    def cone(self, Fade, Colors):
        cursor.setheading(0)
        self.move(0, 0)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.dot(startLength - (startLength / Fade) * x - i)
                cursor.forward(1)
        update()
        reset()

    def doublecone(self, Fade, Colors):
        cursor.setheading(0)
        cursor.width(startLength)
        self.move(-startLength, 0)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.width(width() - 1)
                cursor.forward(1)
        cursor.forward(2)
        cursor.width(1)
        for x in range(Fade):
            C2 = Colors[len(Colors) - x - 1]
            C1 = Colors[len(Colors) - x - 2]
            for i in range(int(startLength / Fade)):
                cursor.width(width() + .25)
                self.change(C1, C2, i, Fade)
                cursor.up()
                cursor.forward(.5)
                cursor.right(90)
                self.Circle((startLength / Fade) * x + i + 1, 360)
                cursor.left(90)
        update()
        reset()

    def yinyang(self, Fade, Colors):
        cursor.setheading(0)
        self.move(0, 0)
        Fade -= 1
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(360 / Fade)):
                self.change(C1, C2, i * startLength / 360, Fade)
                self.Circle(startLength, 180)
                self.Circle(-startLength, 180)
                cursor.left(180)
                self.Circle(startLength, 180)
                self.Circle(-startLength, 180)
                cursor.left(181)
        update()
        reset()

    def heart(self, Fade, Colors):
        self.move(0, 0)
        cursor.setheading(90)
        cursor.shape("Heart")
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.shapesize((startLength - (startLength / Fade) * x - i))
                cursor.stamp()
        update()
        reset()

    def quatre(self, Fade, Colors):
        self.move(0, 0)
        cursor.setheading(180)
        cursor.shape("Quatre")
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, i, Fade)
                cursor.shapesize((startLength - (startLength / Fade) * x - i) / 3)
                cursor.stamp()
        update()
        reset()


Draw = DrawClass()

RADIOS = [("flower", Draw.flower, 1),
          ("circle1", Draw.circle1, 2),
          ("circle2", Draw.circle2, 3),
          ("polygon", Draw.polygon, 4),
          ("polygon-swirl", Draw.polygonswirl, 5),
          ("cone", Draw.cone, 6),
          ("doublecone", Draw.doublecone, 7),
          ("yinyang", Draw.yinyang, 8),
          ("heart", Draw.heart, 9),
          ("quatrefoil", Draw.quatre, 10)]


for name, func, ind in RADIOS:
    Radiobutton(panel, text=name, variable=selectionShape, value=ind, indicatoron=0, command=btn_click)\
        .grid(row=ind, column=0)


def get_shape():
    global selectionShape


Button(panel, text="Get", command=get_shape).grid(row=1, column=2)


def draw():
    global colorC, selectionShape
    sent_matrix = []
    for _x in range(colorC):
        sent_matrix += [colorMatrix[_x]]
    for reverse in range(len(sent_matrix) - 1):
        sent_matrix += [sent_matrix[len(sent_matrix) - (2 * reverse + 2)]]

    RADIOS[selectionShape.get()-1 ][1](colorC - 1, sent_matrix)


def color_buttons(_x):
    global cButtonList, colorC
    _x = int(_x)
    colorC = _x
    for y in range(len(cButtonList)):
        cButtonList[0].grid_remove()
        cButtonList.remove(cButtonList[0])
    for y in range(_x):
        cButtonList += [Button(panel, text="Color " + str(y), command=functools.partial(color_button, y))]
        cButtonList[y].grid(row=12, column=y + 2)


def color_button(color_num):
    global colorMatrix
    temp = askcolor()
    colorMatrix[color_num] = [int(temp[0][0]), int(temp[0][1]), int(temp[0][2])]


cButtonList = [Button(panel, text="OK", command=color_button)]
bu = Button(panel, text="Draw", command=draw)
bu.grid(row=1, column=2, rowspan=3, columnspan=3)
w = Scale(panel, from_=1, to=30, length=300, label="Color Amount", command=color_buttons)
w.grid(row=0, column=1, rowspan=10)

mainloop()
