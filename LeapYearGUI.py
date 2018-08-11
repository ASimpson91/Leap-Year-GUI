
# This program will ask the user to input a year and then will decide
# whether the year entered is a leap year or not a leap year.


from graphics import *

win = GraphWin("Leap Year?", 300, 265)
win.setBackground("cyan")


def main():
    enterButton, entry, usrYearInp, intersectRectangle2, intersectRectangle3 = gui()

    click(enterButton, entry, usrYearInp, intersectRectangle2, intersectRectangle3)


def gui():  # Creates a graphical user interface (GUI) for the program
    inputText = Text(Point(150, 78), "Input year:")  # Displays input year above entry
    inputText.setSize(13)
    inputText.setStyle("bold")
    inputText.draw(win)

    directionText = Text(Point(153, 250), "Enter a year and find out if it is a leap year! ")  # Displays Directions
    directionText.setSize(7)
    directionText.setStyle("bold")
    directionText.draw(win)

    line = Line(Point(58, 60), Point(242, 60))  # Displays a line below the title, leap year
    line.setWidth(3)
    line.draw(win)

    title = Text(Point(150, 40), "LEAP YEAR?")  # Displays the title, "LEAP YEAR"
    title.setSize(22)
    title.setTextColor("blue")
    title.setStyle("bold")
    title.draw(win)

    entry = Entry(Point(150, 110), 20)  # Creates an entry point for the user to type a year
    entry.setFill("white")
    entry.draw(win)

    outRectangle = Rectangle(Point(59, 130), Point(240, 170))  # Creates a spot to display whether the year is a leap
    outRectangle.setWidth(3)                                   # year or not
    outRectangle.setFill("black")
    outRectangle.draw(win)

    intersectRectangle = Rectangle(Point(59, 130), Point(135, 170))  # Displays another rectangle to separate the year
    intersectRectangle.setWidth(3)                                   # from the decision
    intersectRectangle.setFill("black")
    intersectRectangle.setOutline("blue")
    intersectRectangle.draw(win)

    intersectRectangle2 = Rectangle(Point(135,130),Point(189,170))  # Displays another rectangle to separate colors
    intersectRectangle2.setWidth(3)
    intersectRectangle2.setOutline("blue")
    intersectRectangle2.draw(win)

    intersectRectangle3 = Rectangle(Point(189,130),Point(240, 170))  # Displays another rectangle to separate colors
    intersectRectangle3.setWidth(3)
    intersectRectangle3.setOutline("blue")
    intersectRectangle3.setFill("black")
    intersectRectangle3.draw(win)

    yesText = Text(Point(160, 150), "Yes")  # Displays yes and no to notify the user that the year entered
    yesText.setStyle("bold")                # is either a leap year or not
    yesText.setTextColor("white")
    noText = yesText.clone()
    noText.move(55, 0)
    noText.setText("No")
    noText.setTextColor("white")
    noText.setStyle("bold")
    noText.draw(win)
    yesText.draw(win)

    yearDisplay = Text(Point(96, 140), "Year:")  # Displays the year to allow the user to know the year
    yearDisplay.setSize(10)                      # that was entered
    yearDisplay.setTextColor("white")
    yearDisplay.setStyle("bold")
    yearDisplay.draw(win)

    enterButton = Rectangle(Point(59, 180), Point(240, 230))  # Displays the clickable enter button
    enterButton.setWidth(3)
    enterButton.setFill("black")
    enterButton.setOutline("blue")
    enterButton.draw(win)

    buttonText = Text(Point(150, 205), "ENTER")  # Displays the text on the clickable button
    buttonText.setTextColor("white")
    buttonText.setSize(18)
    buttonText.draw(win)

    usrYearInp = Text(Point(96, 156), "")  # Displays the year that the user entered
    usrYearInp.setStyle("bold")
    usrYearInp.setTextColor("white")
    usrYearInp.setSize(10)
    usrYearInp.draw(win)

    leapTrue = Text(Point(185, 152), "")  # Place holder to display that the year is in fact a leap year
    leapTrue.setStyle("bold")
    leapTrue.setSize(10)
    leapTrue.draw(win)

    leapFalse1 = Text(Point(185, 157), "")  # Place holder for part one of the output letting the user know
    leapFalse1.setStyle("bold")             # the year entered is not a leap year
    leapFalse1.setSize(10)
    leapFalse1.draw(win)

    leapFalse2 = Text(Point(185, 142), "")  # Place holder for part one of the output letting the user know
    leapFalse2.setStyle("bold")             # the year entered is not a leap year
    leapFalse2.setSize(10)
    leapFalse2.draw(win)

    return enterButton, entry, usrYearInp, intersectRectangle2, intersectRectangle3


def inside(point, rectangle):  # Allows the user to click inside the enter button
    lowerLeftPoint = rectangle.getP1()
    upperRightPoint = rectangle.getP2()

    return lowerLeftPoint.getX() < point.getX() < upperRightPoint.getX() and lowerLeftPoint.getY() \
           < point.getY() < upperRightPoint.getY()


def click(enterButton, entry, usrYearInp,
          intersectRectangle2, intersectRectangle3):  # executes the click, changes colors of yes and no rectangles
    while True:
        clickPoint = win.getMouse()

        if inside(clickPoint, enterButton):
            b = int(entry.getText())

            divByFour = (b % 4)
            divFourHun = (b % 400)
            divOneHun = (b % 100)

            usrYearInp.setText(b)
            intersectRectangle2.setFill("black")
            intersectRectangle3.setFill("black")
            entry.setText("")

            if divFourHun == 0:
                intersectRectangle2.setFill("green")

            elif divOneHun == 0:
                intersectRectangle3.setFill("red")

            elif divByFour == 0:
                intersectRectangle2.setFill("green")

            else:
                intersectRectangle3.setFill("red")


main()
