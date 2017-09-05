#Greg Phillips
#9/5/17
#slope.py

x1 = float(input("Write x1 value here "))
y1 = float(input("Write y1 value here "))
x2 = float(input("Write x2 value here "))
y2 = float(input("Write y2 value here "))

slope = (y1-y2)/(x1-x2)
print("The slope is", slope)

b = float(y1 - slope*x1)
print("The equation of the line is Y =", slope, "x +", b)