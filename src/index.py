# Author: Elio Di Nino
#
# Date Started: September 10th, 2021
# Date Finished: September 13th, 2021
#
# Purpose: Given points of a line and the data for a circle, this program first validates
# the inputs, and then tells the user at how many points the line and the circle intersect
# (0, 1, or 2 times). It also prints out at which points the intersection(s) occur. The
# program does this by first calculating the slope and equation of the line based of the
# 2 points and then it creates the equation for the circle. Then, these values are
# calculated into the variables for the quadratic equation using math I did shown on the
# README page.
#
# Although the rules only required calculation based off of integers, my program supports
# floating point numbers and also validates the inputted points for correctness/errors.

import math

# Variables for the line (li) and circle (cir) inputs
liX1 = 0
liY1 = 0
liX2 = 0
liY2 = 0

cirX = 0
cirY = 0
cirR = 0

# Boolean variables to track whether or not the inputs given are valid
validLineInputs = False
validCircleInputs = False

# All of the characters needing to be spliced for each object's inputes
liRemoveCharacters = "() "
cirRemoveCharacters = "()r="

# Error messages for each respective input
lineErrorResponse = "\nYour input is incorrect. Please try again following this guide:\n(#,#), (#,#)\n"
circleErrorResponse = "\nYour input is incorrect. Please try again following this guide:\n(#,#) r=#\n"

# Get the values for the line from the user. Repeat until the input is valid.
while validLineInputs == False:
    # Ask for input
    line = str(input("Line: "))
    # Make sure there are 2 "(" and 2 ")"
    if line.count("(") == 2 and line.count(")") == 2:
        # Remove irrelevant characters
        for char in liRemoveCharacters:
            line = line.replace(char,"")
        # Splice the inputs at every ","
        parse = line.split(",")
        # See if there are 4 separate values
        if len(parse) == 4:
            # Cycle through each value
            for i in parse:
                # Temporarily remove any "-" and "." to see if the remaining characters are digits
                if i.replace("-","",1).replace(".","",1).isdigit():
                    i = float(i)
                    validLineInputs = True
                # If any value isn't valid, break from the loop, send the error message, and request the input again
                else:
                    validLineInputs = False
                    print(lineErrorResponse)
                    break
            # See if the two points provided are the same
            if parse[0] == parse[2] and parse[1] == parse[3]:
                validLineInputs = False
                print("The same point cannot be provided twice. Please try again.")
            # See if the inputs provided didn't form a function
            elif parse[0] == parse[2]:
                validLineInputs = False
                print("The same X value cannot be associated with 2 Y values, otherwise it is no longer a function.")
        else:
            print(lineErrorResponse)
            break
    else:
        print(lineErrorResponse)

# Save the parsed values into separate variables defined previously
liX1 = float(parse[0])
liY1 = float(parse[1])
liX2 = float(parse[2])
liY2 = float(parse[3])

# Get the values for the line from the user. Repeat until the input is valid.
while validCircleInputs == False:
    # Ask for input
    circle = str(input("Circle: "))
    # Make sure there is 1 " ", 1 "(", 1 ")" and 1 "r="
    if circle.count(" ") == 1 and circle.count("(") == 1 and circle.count(")") == 1 and circle.count("r=") == 1:
        # Change the "," to a " " for splicing later
        circle = circle.replace(","," ")
        # Remove irrelevant characters
        for char in cirRemoveCharacters:
            circle = circle.replace(char,"")
        # Splice the inputs at every " "
        parse = circle.split(" ")
        # See if there are 3 separate values
        if len(parse) == 3:
            # Cycle through each value
            for i in parse:
                # Temporarily remove any "-" and "." to see if the remaining characters are digits
                if i.replace("-","",1).replace(".","",1).isdigit():
                    i = float(i)
                    validCircleInputs = True
                # If any value isn't valid, break from the loop, send the error message, and request the input again
                else:
                    validCircleInputs = False
                    print(circleErrorResponse)
                    break
                # If the 3rd value (the radius) is <= 0, ask for it again
                if i == float(parse[2]) and i <= 0:
                    print("The radius (r) must be greater than 0. Please try again.")
                    validCircleInputs = False
                    break
        else:
            print(circleErrorResponse)
            break
    else:
        print(circleErrorResponse)

# Save the parsed values into separate variables defined previously
cirX = float(parse[0])
cirY = float(parse[1])
cirR = float(parse[2])

# Calculate the slope of the line (m)
def slope(liX1,liY1,liX2,liY2):
    m = (liY2 - liY1) / (liX2 - liX1)
    return m

# Calculate the y-intercept of the line (b)
def yInt(liMX,liX1,liY1):
    b = liY1 - (liMX * liX1)
    return b

# Calculate whether or not there is an intersection
def intersect(liMX,yInt,cirX,cirY,cirR):
    # Calculate the individual parts of the quadratic equation (a, b, and c)
    b = (2 * liMX * (yInt - cirY)) - ((2 * cirX))
    a = liMX**2 + 1
    c = cirX**2 + (yInt - cirY)**2 - cirR**2
    # Calculate the discriminant to find out how many solutions exist
    discriminant = (b**2) - (4 * a * c)
    # If the discriminant is less than 0, there are 0 solutions
    if discriminant < 0:
        # Print the result
        print("No intersection")
    # If the discriminant equals 0, then there is one solution
    elif discriminant == 0:
        # Calculate the x and y values of the point of intersection
        # For x, using the quadratic formula without the descriminant (because it = 0)
        # For y, using the x that was just found and plugging it into the line's function
        x = -b / (2 * a)
        y = liMX * x + yInt
        # Print the result
        print("One intersection\nPoint: ({:.3f},{:.3f})".format(round(x,3),round(y,3)))
    # If the discriminant is greater than 0, then there are two solutions
    else:
        # Calculate the x and y values of the points of intersection
        # For x, using the quadratic formula with the descriminant (+- sqrt(b^2 - 4ac)
        # For y, using the x's that were found and plugging them into the line's function
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        y1 = liMX * x1 + yInt
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        y2 = liMX * x2 + yInt
        # Print the result
        print("Two intersections\nPoints: ({:.3f},{:.3f}), ({:.3f},{:.3f})".format(round(x1,3),round(y1,3),round(x2,3),round(y2,3)))
    return

# Run the previously defined functions
liMX = slope(liX1,liY1,liX2,liY2)
yInt = yInt(liMX,liX1,liY1)
intersect(liMX,yInt,cirX,cirY,cirR)
