#################################################################################
######                           Imports                                    #####
#################################################################################
from turtle import*
import re
import math
import time
import shapeDefinitions
#################################################################################
######                       Variable Setup                                 #####
#################################################################################
tracer(36000)
global startLength
startLength=360
colormode(255)
speed(1)
shapeOptions = ["flower","circle1","circle2","polygon","polygon-swirl","cone","doublecone","yinyang","heart","quatrefoil"]
shapeFade=[1,1,1,1,1,1,0,0,1,1]
preset=False
up()
begin_poly()
forward(1)
for l in range(4):
    circle(1,270,200)
    left(180)
end_poly()
register_shape("Quatre",get_poly())
goto(0,0)
up()
setheading(90)
begin_poly()
backward(.707)
right(30)
forward(1)
left(30)
circle(.25,180,120)
left(180)
circle(.25,180,120)
left(30)
forward(1)
end_poly()
register_shape("Heart",get_poly())
#################################################################################
######                       Function Setup                                 #####
#################################################################################
            
#################################################################################
######                          Execution                                   #####
#################################################################################
Draw=shapeDefinitions.shapes()
while True:
    clear()
    width(12)
    update()
    shapeType = -1
    colorMatrix=[[]]
    gradientCount=-.1
    shapeInput="Temporary"
    hideturtle()
    while gradientCount<=0 or gradientCount != int(gradientCount):        ##This block gets an input of the amount of gradients, confirms they are a positive integer, and saves it to gradientCount
        gradientCount=str(input("How many gradients would you like?(one gradient is 2 colors, 2 gradients is 3 colors etc): "))
        if not gradientCount.isnumeric():
            gradientCount=-1
        else:
            gradientCount=int(gradientCount)

    print("Format is 'R,G,B' , include commas")
    for x in range(gradientCount+1):
        colorListString="abc"
        while True:
            print("Color number",x+1,": ")
            colorListString=input()
            if all(x <= 3 for x in [len(i) if int(i) >= 0 and int(i) <= 255 else 4 for i in colorListString.split(',')]) and colorListString.count(",")==2:
                break ##Makes sure the format is 0-255,0-255,0-255

        colorList=colorListString.split(",")    ##Format string into a list
        for i in range(3):
            colorList[i]=int(colorList[i])
        colorMatrix+=[colorList]
    colorMatrix.remove([])
    print(colorMatrix)

    while shapeType==-1:
        print("Available shapes:" )
        print("flower, circle1, circle2, polygon, polygon-swirl, cone,")
        print("doublecone, yinyang, heart, quatrefoil" )
        while shapeOptions.count(shapeInput) ==0:
            shapeInput=input("Which would you like? ")
            for item in shapeOptions:
                if (item.find('abc')) != -1:
                    break
        shapeType = shapeOptions.index(shapeInput)
    if shapeFade[shapeType]==1:
        print("1=Fade from color 1 to color 2")
        print("2=Start at color 1, going to the last color and back to the first")
        Fade="Temporary"
        while not Fade.isnumeric():
            Fade=input("Fade Format: ")
        Fade=(int)(Fade)
        for reverse in range(len(colorMatrix)-1):
            colorMatrix+=[colorMatrix[len(colorMatrix)-(2*reverse+2)]]
    Fade*=gradientCount
    print(colorMatrix)
    shapeType+=1
    start=time.time()
    functions = {1:Draw.flower,2:Draw.circle1,3:Draw.circle2,4:Draw.polygon,
                 5:Draw.polygonswirl,6:Draw.cone,7:Draw.doublecone,8:Draw.yinyang,9:Draw.heart,10:Draw.quatre}
    functions[shapeType](Fade,colorMatrix)
    end=time.time()
    print(end-start)
