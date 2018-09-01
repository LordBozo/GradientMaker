from turtle import*
class shapes:

    def __init__(x):  ## Initialize global variables
        global cursor
        global startLength
        cursor=Turtle()
        startLength=screensize()[1]
        
    def change(C1,C2,i,Fade): ##This calculates the difference between the colors that its going between, and finds out how much it needs to change each time
        distance=startLength/Fade
        red=int(C1[0]+ ((C2[0]-C1[0])/distance) *i)
        green=int(C1[1]+ ((C2[1]-C1[1])/distance) *i)
        blue=int(C1[2]+ ((C2[2]-C1[2])/distance) *i)
        cursor.color((red,green,blue))
    def move(x,y):  ##moves the turtle somewhere without leaving a line
        cursor.up()
        cursor.goto(x,y)
        cursor.down()
    def Circle(radius,degree): ## Custom Circle function cuz Turtle's default one is really slow and poorly optimized for smaller sizes
        cursor.down()
        mult=radius/abs(radius)
        for x in range(int(degree/2)):
            cursor.left(mult)
            cursor.forward((2*math.pi*radius)/360)
            cursor.left(mult)

################################################################################
######                     Shape Definitions                               #####
################################################################################
            
    def flower(Fade,Colors):
        shapes.move(startLength/2,0)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.forward(startLength-(startLength/Fade)*x-i)
                cursor.right(105)
            
    def circle1(Fade,Colors):
        cursor.pensize(4)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                shapes.Circle(startLength,180)
                shapes.Circle(-startLength,180)
                cursor.right(360/startLength)

    def circle2(Fade,Colors):
        cursor.left(90)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.dot(startLength-(startLength/Fade)*x-i)
                cursor.forward(1/(10*startLength))

    def polygon(Fade,Colors):
        print("How many sides do you want on your polygon?")
        Point=int(input())
        cursor.up()
        cursor.goto(math.cos(0),math.sin(0))
        cursor.begin_poly()
        for p in range(Point):
            cursor.goto(math.cos(math.radians(360/Point)*p),math.sin(math.radians(360/Point)*p))
        cursor.end_poly()
        register_shape("Polygon",cursor.get_poly())
        cursor.down()
        cursor.shape("Polygon")
        cursor.setheading(90)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.shapesize(startLength-(startLength/Fade)*x-i)
                cursor.stamp()

    def polygonswirl(Fade,Colors):
        print("How many sides do you want on your polygon?")
        Point=int(input())
        print("How many degrees do you want to rotate each time?")
        Rotate=float(input())
        cursor.up()
        cursor.goto(math.cos(0),math.sin(0))
        cursor.begin_poly()
        for p in range(Point):
            cursor.goto(math.cos(math.radians(360/Point)*p),math.sin(math.radians(360/Point)*p))
        cursor.end_poly()
        register_shape("Polygon",cursor.get_poly())
        cursor.down()
        cursor.shape("Polygon")
        cursor.setheading(90)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.shapesize(startLength-(startLength/Fade)*x-i)
                cursor.stamp()
                cursor.right(Rotate)

    def cone(Fade,Colors):
        cursor.setheading(0)
        cursor.move(0,0)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.dot(startLength-(startLength/Fade)*x-i)
                cursor.forward(1)    

    def doublecone(Fade,Colors):
        cursor.setheading(0)
        cursor.width(startLength)
        shapes.move(-startLength,0)
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.width(width()-1)
                cursor.forward(1)
        cursor.forward(2)
        cursor.width(1)
        for x in range(Fade):
            C2=Colors[len(Colors)-x-1]
            C1=Colors[len(Colors)-x-2]
            for i in range(int(startLength/Fade)):
                cusor.width(width()+.125)
                shapes.change(C1,C2,i,Fade)
                cursor.up()
                cursor.forward(.5)
                cursor.right(90)
                shapes.Circle((startLength/Fade)*x+i+1,360)
                cursor.left(90)

    def yinyang(Fade,Colors):
        cursor.setheading(0)
        shapes.move(0,0)
        Fade-=1
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(360/Fade)):
                shapes.change(C1,C2,i*startLength/360,Fade)
                shapes.Circle(startLength,180)
                shapes.Circle(-startLength,180)
                cursor.left(180)
                shapes.Circle(startLength,180)
                shapes.Circle(-startLength,180)
                cursor.left(181)

    def heart(X,Fade,Colors):
        shapes.move(0,0)
        cursor.setheading(90)
        cursor.shape("Heart")
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.shapesize((startLength-(startLength/Fade)*x-i))
                cursor.stamp()
                
    def quatre(Fade,Colors):
        shapes.move(0,0)
        cursor.setheading(180)
        cursor.shape("Quatre")
        for x in range(Fade):
            C1=Colors[x]
            C2=Colors[x+1]
            for i in range(int(startLength/Fade)):
                shapes.change(C1,C2,i,Fade)
                cursor.shapesize((startLength-(startLength/Fade)*x-i)/3)
                cursor.stamp()
