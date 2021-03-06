##Special thanks to ThePhisics101 for helping fix some buttons on the GUI

from tkinter import *
from turtle import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *
import functools
import math
panel = Tk()
cv=Canvas(panel,width=panel.winfo_screenheight()-100,height=panel.winfo_screenheight()-100)
cv.grid(row=0,column=0,rowspan=30)
selectionShape = IntVar()
colorMatrix = []
colorC = 0
for x in range(150):
    colorMatrix += [[0, 0, 0]]

def btn_click():
    get_shape()
class DrawClass(object):
    def __init__(self):  
        global cursor, startLength,screen
        startLength = 100
        cursor = RawTurtle(cv)
        screen=cursor.getscreen()
        screen.colormode(255)
        screen.tracer(1000)
        cursor.up()
        cursor.begin_poly()
        cursor.forward(1)
        for l in range(4):
            cursor.circle(1,270,200)
            cursor.left(180)
        cursor.end_poly()
        screen.register_shape("Quatre",cursor.get_poly())
        cursor.goto(0,0)
        cursor.up()
        cursor.setheading(90)
        cursor.begin_poly()
        cursor.backward(.707)
        cursor.right(30)
        cursor.forward(1)
        cursor.left(30)
        cursor.circle(.25,180,200)
        cursor.left(180)
        cursor.circle(.25,180,200)
        cursor.left(30)
        cursor.forward(1)
        cursor.end_poly()
        screen.register_shape("Heart",cursor.get_poly())
        cursor.width(12)
        cursor.hideturtle()

    def change(self, C1, C2, percent):  ##This calculates the difference between the colors that its going between, and finds out how much it needs to change each time
        red = int(C1[0] + ((C2[0] - C1[0]) / 100) * percent)
        green = int(C1[1] + ((C2[1] - C1[1]) / 100) * percent)
        blue = int(C1[2] + ((C2[2] - C1[2]) / 100) * percent)
        #print(percent,C1,C2)
        cursor.color((red, green, blue))

    def move(self, x, y):  ##moves the turtle somewhere without leaving a line
        cursor.up()
        cursor.goto(x, y)
        cursor.down()

    def Circle(self, radius, degree):  ## Custom Circle function cuz Turtle's default one is really slow and poorly optimized for smaller sizes
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
        cursor.up()
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.forward(.5*(startLength - (startLength / Fade) * x - i))
                cursor.down()
                cursor.forward(.5*(startLength - (startLength / Fade) * x - i))
                cursor.right(105)
        screen.update()
         

    def circle1(self, Fade, Colors):
        self.move(0, 0)
        cursor.width(5)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(180 / Fade)):
                self.change(C1, C2, i/(1.80/Fade) )
                self.Circle(startLength, 180)
                self.Circle(-startLength, 180)
                cursor.right(2)
        screen.update()
         

    def circle2(self, Fade, Colors):
        cursor.left(90)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.dot(2*(startLength - (startLength / Fade) * x - i))
                cursor.forward(1 / (10 * startLength))
        screen.update()
         

    def polygon(self, Fade, Colors):
        Point=-1
        while Point==-1:
            Point = askinteger("Polygon", "How many sides do you want",initialvalue=3)
        cursor.up()
        cursor.goto(math.cos(0), math.sin(0))
        cursor.begin_poly()
        for p in range(Point):
            cursor.goto(math.cos(math.radians(360 / Point) * p), math.sin(math.radians(360 / Point) * p))
        cursor.end_poly()
        screen.register_shape("Polygon", cursor.get_poly())
        cursor.down()
        cursor.shape("Polygon")
        cursor.setheading(90)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.shapesize(startLength - (startLength / Fade) * x - i)
                cursor.stamp()
        screen.update()
         

    def polygonswirl(self, Fade, Colors):
        Point=-1
        while Point==-1:
            Point = askinteger("Polygon", "How many sides do you want",initialvalue=3)
        Rotate=-1
        while Rotate==-1:
            Rotate = askinteger("Polygon", "How many degrees do you want it to rotate total",initialvalue=360)
        Rotate/=startLength
        cursor.up()
        cursor.goto(math.cos(0), math.sin(0))
        cursor.begin_poly()
        for p in range(Point):
            cursor.goto(math.cos(math.radians(360 / Point) * p), math.sin(math.radians(360 / Point) * p))
        cursor.end_poly()
        screen.register_shape("Polygon", cursor.get_poly())
        cursor.down()
        cursor.shape("Polygon")
        cursor.setheading(90)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.shapesize(startLength - (startLength / Fade) * x - i)
                cursor.stamp()
                cursor.right(Rotate)
        screen.update()
        

    def cone(self, Fade, Colors):
        cursor.width(1)
        cursor.setheading(0)
        self.move(0, 0)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.dot(startLength - (startLength / Fade) * x - i)
                cursor.forward(1)
        screen.update()
         

    def doublecone(self, Fade, Colors):
        sL=startLength/1.75
        cursor.width(1)
        cursor.setheading(0)
        self.move(-startLength/1.75, 0)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.dot((startLength - (startLength / Fade) * x - i)/1.75)
                cursor.forward(.5)
        cursor.forward(2)
        cursor.width(1)
        for x in range(Fade):
            C2 = Colors[len(Colors) - x - 1]
            C1 = Colors[len(Colors) - x - 2]
            for i in range(int(sL / Fade)):
                cursor.width(cursor.width() + 2/sL)
                self.change(C2, C1, 100*i*Fade/sL)
                cursor.up()
                cursor.forward(.5)
                cursor.right(90)
                self.Circle((sL / Fade) * x + i + 1, 360)
                cursor.left(90)
        screen.update()
         

    def yinyang(self, Fade, Colors):
        self.move(0, 0)
        cursor.pensize(8)
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(90/Fade)):
                self.change(C1, C2, i/(.90/Fade))
                self.Circle(startLength, 180)
                self.Circle(-startLength, 180)
                cursor.right(180)
                self.Circle(startLength, 180)
                self.Circle(-startLength, 180)
                cursor.right(182)
        screen.update()
         

    def heart(self, Fade, Colors):
        self.move(0, 100)
        cursor.setheading(90)
        cursor.shape("Heart")
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.shapesize(1.5*(startLength - (startLength / Fade) * x - i))
                cursor.stamp()
        screen.update()

    def quatre(self, Fade, Colors):
        self.move(0, 0)
        cursor.setheading(180)
        cursor.shape("Quatre")
        for x in range(Fade):
            C1 = Colors[x]
            C2 = Colors[x + 1]
            for i in range(int(startLength / Fade)):
                self.change(C1, C2, 100*i*Fade/startLength)
                cursor.shapesize(1.2*(startLength - (startLength / Fade) * x - i) / 3)
                cursor.stamp()
        screen.update()

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
    Radiobutton(panel, text=name, variable=selectionShape, value=ind, indicatoron=0, command=btn_click).grid(row=ind, column=1)

def get_shape():
    global selectionShape

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
        rgb=colorMatrix[y]
        if rgb==[0,0,0]:
            rgb=[255,255,255]
        tempRGB=f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
        cButtonList += [Button(panel, text="Color " + str(y+1),bg=tempRGB, command=functools.partial(color_button, y))]
        cButtonList[y].grid(row=10, column=y + 2)

def color_button(color_num):
    global colorMatrix
    temp = askcolor()
    cButtonList[color_num].config(bg=temp[1])
    temp=temp[0]
    colorMatrix[color_num] = [int(temp[0]), int(temp[1]), int(temp[2])]
def clear_button():
    cursor.reset()
    cursor.width(12)
    cursor.shape("classic")
    cursor.hideturtle()
def size(x):
    global startLength
    startLength=int(x)
cButtonList = [Button(panel, text="OK", command=color_button)]
bu = Button(panel, text="Draw", command=draw, height=4, width=8)
bu.grid(row=1, column=3,rowspan=3,columnspan=3)
bu = Button(panel, text="Erase", command=clear_button)
bu.grid(row=5, column=3)
w = Scale(panel, from_=1, to=30, length=300, label="Color Amount", command=color_buttons)
w.grid(row=11, column=1, rowspan=10)
w = Scale(panel, from_=100, to=(panel.winfo_screenheight()-100)/2, length=300, label="Size", command=size)
w.grid(row=11, column=2, rowspan=10)

mainloop()
