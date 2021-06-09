def inputCheck():
    while True:
        floatNum = input("Input: ")
        try:
            floatNum = float(floatNum)
            break
        except ValueError:
            print("That's not a number! Enter a valid input.")
    return floatNum

#discriminant finder
def findDiscriminant(a,b,c):
    if a < 0.0:
        print("Parabola opens downward.")
    else:
        print("Parabola opens upward.")
    discriminant = (b**2)-(4*a*c)
    if discriminant > 0:
        print(f"Equation has 2 real, distinct roots. Y-intercept is y = {str(c)}.")
        sol1 = (- b + math.sqrt(discriminant))/(2*a)
        sol2 = (- b - math.sqrt(discriminant))/(2*a)
        print(f"The roots are x = {str(round(sol1,2))} and x = {str(round(sol2,2))} (Note all values are rounded)")
    elif discriminant == 0:
        print(f"Equation has 2 real, equal roots.Y-intercept is y = {str(c)}.")
        sol = (- b - math.sqrt(discriminant))/(2*a)
        print(f"The root is x = {str(round(sol,3))}.")
    elif discriminant < 0:
        print(f"Equation has no real roots. Y-intercept is y = {str(c)}.")

#find coordinates
def findCoordinates(minX,maxX,a,b,c):
    x = minX
    xList = []
    yList = []
    cordsTable = PrettyTable(["x","y"])
    print("Coordinates for graph are below in format (x,y).")
    while maxX >= x >= minX:
        xCord = x
        xList.append(xCord)
        yCord = a*x**2 + b*x + c
        yList.append(yCord)
        cordsTable.add_row([str(xCord),str(yCord)])
        x+=1
    print(cordsTable)
    plt.plot(xList,yList)
    plt.show()
