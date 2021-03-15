import math as mt
import numpy as np
import matplotlib.pyplot as plt

#loading input file
print("\n","Data Requirements:", "\n",
    "1. Your data should be two column data", "\n",
    "2. Your data should have extension .txt","\n"
    )
userInput = input("Enter your input filename with extension (ex: input.txt): ")
fileInput = np.loadtxt(userInput)

#defining
inputX = np.array(fileInput[:,0])
inputY = np.array(fileInput[:,1])

#length
lengthX = len(inputX)
lengthY = len(inputY)

#sum
sumX = np.sum(inputX)
sumY = np.sum(inputY)

#XY
inputXY = np.multiply(inputX, inputY)

#sum of XY
sumInputXY = np.sum(inputXY)

#mean
meanX = sumX / lengthX
meanY = sumY / lengthY

#square of sum
squareSumX = np.multiply(sumX, sumX)
squareSumY = np.multiply(sumY, sumY)

#square of each
squareX = np.multiply(inputX, inputX)
squareY = np.multiply(inputY, inputY)

#sum of square
sumSquareX = np.sum(squareX)
sumSquareY = np.sum(squareY)

#root mean square
rmsX = mt.sqrt((sumSquareX / lengthX))
rmsY = mt.sqrt((sumSquareY / lengthY))

#variance
varX1 = np.subtract(inputX, meanX)
varX2 = np.multiply(varX1, varX1)
varX3 = np.sum(varX2)
varX = varX3 / (lengthX - 1)

varY1 = np.subtract(inputY, meanY)
varY2 = np.multiply(varY1, varY1)
varY3 = np.sum(varY2)
varY = varY3 / (lengthY - 1)

#standard deviation
sX = mt.sqrt(varX)
sY = mt.sqrt(varY)

#covariance
cov1 = np.multiply(varX1, varY1)
cov2 = np.sum(cov1)
cov = cov2 / (lengthX - 1)

#pearson product-moment correlation coefficient
r1 = np.multiply(sumX, sumY)
r2 = np.multiply(lengthX, sumInputXY)
r3 = np.subtract(r2, r1)
r4 = np.multiply(sumSquareX, lengthX)
r5 = np.multiply(sumSquareY, lengthY)
r6 = np.subtract(r4, squareSumX)
r7 = np.subtract(r5, squareSumY)
r8 = np.multiply(r6, r7)
r9 = mt.sqrt(r8)
r = r3 / r9

#determination coefficient
r2 = np.multiply(r, r)

#linear regression
b = cov2 / varX3

a1 = np.multiply(b, sumX)
a2 = np.subtract(sumY, a1)
a = a2 / lengthX

bEq = ""
aEq = ""

if b == 1 :
    bEq = "X"
elif b == 0 :
    bEq = ""
elif b == -1 :
    bEq = "- X"
else :
    bEq = str(b) + "X"

if a > 0 :
    aEq = "+" + " " + str(a)
elif a == 0 :
    aEq = ""
elif a < 0 :
    aEq = "-" + " " + str(abs(a))
else :
    aEq = str(a)

eq = "Y = " + bEq + " " + aEq

plotY1 = np.multiply(b, inputX)
plotY = np.add(plotY1, a)

#displaying data
print("\n", "The Input X:", "\n", inputX)
print("\n", "The Input Y:", "\n", inputY)
print("\n", "The Length of X:", "\n", lengthX)
print("\n", "The Length of Y:", "\n", lengthY)
print("\n", "The Sum of X:", "\n", sumX)
print("\n", "The Sum of Y:", "\n", sumY)
print("\n", "The XY:", "\n", inputXY)
print("\n", "The Sum of XY:", "\n", sumInputXY)
print("\n", "The Mean of X:", "\n", meanX)
print("\n", "The Mean of Y:", "\n", meanY)
print("\n", "The Square of Sum X:", "\n", squareSumX)
print("\n", "The Square of Sum Y:", "\n", squareSumY)
print("\n", "The Square of Each X:", "\n", squareX)
print("\n", "The Square of Each Y:", "\n", squareY)
print("\n", "The Sum of Square of Each X:", "\n", sumSquareX)
print("\n", "The Sum of Square of Each Y:", "\n", sumSquareY)
print("\n", "The Root Mean Square of X:", "\n", rmsX)
print("\n", "The Root Mean Square of Y:", "\n", rmsY)
print("\n", "The Variance of X:", "\n", varX)
print("\n", "The Variance of Y:", "\n", varY)
print("\n", "The Standard Deviation of X:", "\n", sX)
print("\n", "The Standard Deviation of Y:", "\n", sY)
print("\n", "The Covariance:", "\n", cov)
print("\n", "The Pearson Product-Moment Correlation Coefficient:", "\n", r)
print("\n", "The Determination Coefficient:", "\n", r2)
print("\n", "The Slope of Linear Regression Line:", "\n", b)
print("\n", "The Intercept of Linear Regression Line:", "\n", a)
print("\n", "The Linear Regression Equation:", "\n", eq)

#ploting data
plt.plot(inputX, inputY, "o", label = "Data", ms = "10", mec = "midnightblue", mfc = "dodgerblue")
plt.plot(inputX, plotY, ls = "-", label = "Regression Line", color = "#1D1D1D", linewidth = "2")
plt.legend(loc="upper right")

plt.grid()

font1 = {"family":"serif","color":"#1D1D1D","size":20}
font2 = {"family":"serif","color":"#1D1D1D","size":15}

plt.xlabel("The Input X", fontdict = font2)
plt.ylabel("The Input Y", fontdict = font2)
plt.title("Linear Regression Plot", fontdict = font1)
plt.show()