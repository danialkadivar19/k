class mypoint:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
p1=mypoint()
class Rectangle:
    def __init__(self,corner,w=10,h=5):
        self.corner=p1
        self.w=w
        self.h=h
    def ispoint(a,b):
        if 0<=a<10 and 0<=b<5:
            print('noghte dar mostatil hast')
        else:
            print('noghte dar mostatil nist')    

a=float(input('tol noghte:'))
b=float(input('arz noghte:'))
Rectangle.ispoint(a,b)

''' Write a new method in the Rectangle class to test if a Point falls within
the rectangle. For this exercise, assume that a rectangle at (0,0) with
width 10 and height 5 has open upper bounds on the width and height,
i.e. it stretches in the x direction from [0 to 10), where 0 is included but
10 is excluded, and from [0 to 5) in the y direction. So it does not contain
the point (10, 2)'''  

