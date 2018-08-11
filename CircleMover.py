
# This project will ask the user to click the screen twice creating two points. It will then find the radius of that
# point and create a circle. Once the circle is created it will then ask the user to make five more circles by just
# clicking once and creating a center point.

import math
import graphics
import time
from graphics import *
win = graphics.GraphWin("Circle Movement", 500, 500)


def main():

    txt, px,py,p = pointOne()
    p2x,p2y,p2 = pointTwo(txt)
    
    center,pCx,pCy,radius,circ = trig(px,py,p2x,p2y,txt)
    move(center,txt,pCx,pCy,radius,circ,p,p2)
    

def pointOne():
    
    txt = Text(Point(247,16), "Enter the first point by clicking on the screen")
    txt.draw(win)

    p = win.getMouse()
    px = p.getX()
    py = p.getY()
    p.draw(win)

    print("Point 1 - x:", px, "y:", py)

    return txt, px,py,p

    
    
def pointTwo(txt):

    txt.setText("Enter the second point by clicking across from the first point")
    
    p2 = win.getMouse()
    p2x = p2.getX()
    p2y = p2.getY()
    p2.draw(win)

    print("Point 2 - x:", p2x, "y:", p2y)

    return p2x,p2y,p2
    
def trig(px,py,p2x,p2y,txt):

    pCx = ((px + p2x) / 2)
    pCy = ((py + p2y) / 2)

    radius = math.sqrt(((px - pCx) ** 2) + ((py - pCy) ** 2))

    center = Point(pCx, pCy)

    print("Original circle center point - x:", pCx, "y:", pCy)

    circ = Circle(center, radius)
    circ.setFill('red')
    circ.draw(win)

    return center,pCx,pCy,radius,circ

    
def move(center,txt,pCx,pCy,radius,circ,p,p2):
    
    txt.setText("Click the new center point")
    
    p3 = win.getMouse()
    p3x = p3.getX()
    p3y = p3.getY()
    cent = Point(p3x, p3y)

    print("Circle 1 center point - x:", p3x, "y:", p3y)

    circle = Circle(cent, radius)
    circle.setFill('red')
    circle.draw(win)
    circ.undraw()

    p.undraw()
    p2.undraw()

    p4 = win.getMouse()
    p4x = p4.getX()
    p4y = p4.getY()
    cent = Point(p4x, p4y)

    print("Circle 2 center point - x:", p4x, "y:", p4y)

    circle1 = Circle(cent, radius)
    circle1.setFill('red')
    circle1.draw(win)
    circle.undraw()

    p5 = win.getMouse()
    p5x = p5.getX()
    p5y = p5.getY()
    cent = Point(p5x, p5y)

    print("Circle 3 center point - x:", p5x, "y:", p5y)

    circle2 = Circle(cent, radius)
    circle2.setFill('red')
    circle2.draw(win)
    circle1.undraw()

    p6 = win.getMouse()
    p6x = p6.getX()
    p6y = p6.getY()
    cent = Point(p6x, p6y)

    print("Circle 4 center point - x:", p6x, "y:", p6y)

    circle3 = Circle(cent, radius)
    circle3.setFill('red')
    circle3.draw(win)
    circle2.undraw()

    p7 = win.getMouse()
    p7x = p7.getX()
    p7y = p7.getY()
    cent = Point(p7x, p7y)
    print("Circle 5 center point - x:", p7x, "y:", p7y)

    circle4 = Circle(cent, radius)
    circle4.setFill('red')
    circle4.draw(win)
    circle3.undraw()

    txt.setText("Finished")
    
main()
