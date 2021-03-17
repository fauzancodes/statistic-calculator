import math as mt
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as sts

#loading input file
print("\n","Data Requirements:", "\n",
    "1. Your data should be three column data with the same length", "\n",
    "2. One column for X-axis, one column for Y-axis, one column for color bar","\n",
    "3. Your data should have extension .txt or .dat","\n"
    )

userInput = input("Enter your input filename with extension (ex: input.txt): ")
columnX = input("The data for the X-axis are in column (ex: 1 or 2 or etc.): ")
columnY = input("The data for the Y-axis are in column (ex: 1 or 2 or etc.): ")
columnColorbar = input("The data for the color bar are in column (ex: 1 or 2 or etc.): ")

fileInput = np.loadtxt(userInput)

#defining
inputX = np.array(fileInput[:, (int(columnX) - 1)])
inputY = np.array(fileInput[:, (int(columnY) - 1)])
colorbar = np.array(fileInput[:, (int(columnColorbar) - 1)])

#length
lengthX = len(inputX)
lengthY = len(inputY)

#median
medianX = np.median(inputX)
medianY = np.median(inputY)

#mode
modeX = sts.mode(inputX)
modeY = sts.mode(inputY)

#sum
sumX = np.sum(inputX)
sumY = np.sum(inputY)

#XY
inputXY = np.multiply(inputX, inputY)

#sum of XY
sumInputXY = np.sum(inputXY)

#mean
meanX = sumX / lengthX #meanX = np.mean(inputX)
meanY = sumY / lengthY #meanY = np.mean(inputY)

#square of sum
squareSumX = sumX * sumX
squareSumY = sumY * sumY

#square of each
squareX = np.multiply(inputX, inputX)
squareY = np.multiply(inputY, inputY)

#sum of square
sumSquareX = np.sum(squareX)
sumSquareY = np.sum(squareY)

#root mean square
rmsX = sumSquareX / lengthX
rmsY = sumSquareY / lengthY

#variance
varX = (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputX, meanX)))) / (lengthX - 1) #varX = np.var(inputX)
varY = (np.sum(np.multiply(np.subtract(inputY, meanY), np.subtract(inputY, meanY)))) / (lengthY - 1) #varY = np.var(inputY)

#standard deviation
sX = mt.sqrt(varX) #sX = np.std(inputX)
sY = mt.sqrt(varY) #sY = np.std(inputY)

#covariance
cov = (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputY, meanY)))) / (lengthX - 1)

#pearson product-moment correlation coefficient
r = (np.subtract((lengthX * sumInputXY), (sumX * sumY))) / (mt.sqrt(((sumSquareX * lengthX) - squareSumX) * ((sumSquareY * lengthY) - squareSumY)))

#determination coefficient
r2 = r * r

#linear regression
b = (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputY, meanY)))) / (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputX, meanX))))

a = (sumY - (b * sumX)) / lengthX

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

plotY = np.add(np.multiply(b, inputX), a)

#simple script for linear regression
"""
slope, intercept, r, p, std_err = stats.linregress(inputX, inputY)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, inputX))

plt.scatter(inputX, inputY)
plt.plot(inputX, mymodel)
plt.show()
"""

#displaying data
print("\n", "The Input X:", "\n", inputX)
print("\n", "The Input Y:", "\n", inputY)
print("\n", "The Length of X:", "\n", lengthX)
print("\n", "The Length of Y:", "\n", lengthY)
print("\n", "The Median of X:", "\n", medianX)
print("\n", "The Median of Y:", "\n", medianY)
print("\n", "The Mode of X:", "\n", modeX)
print("\n", "The Mode of Y:", "\n", modeY)
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
print("\n")
xLabel = input("Enter the label of X-axis for the linear regression plot: ")
yLabel = input("Enter the label of Y-axis for the linear regression plot: ")
cLabel = input("Enter the label of color bar for the linear regression plot: ")
print("\n")

if b == 1 :
    bEqL = "X"
elif b == 0 :
    bEqL = ""
elif b == -1 :
    bEqL = "- X"
else :
    bEqL = str(np.around(b, 3)) + "X"

if a > 0 :
    aEqL = "+" + " " + str(np.around(a, 3))
elif a == 0 :
    aEqL = ""
elif a < 0 :
    aEqL = "-" + " " + str(np.around(abs(a), 3))
else :
    aEqL = str(np.around(a, 3))

eqL = "Y = " + bEqL + " " + aEqL

plt.scatter(inputX, inputY, c = colorbar, cmap = "rainbow")
plt.plot(inputX, plotY, ls = "-", label = eqL, color = "#1D1D1D", linewidth = "1")

plt.legend(loc="lower right")

plt.grid()

font1 = {"family":"serif","color":"#1D1D1D","size":20}
font2 = {"family":"serif","color":"#1D1D1D","size":15}

plt.colorbar().ax.set_ylabel(cLabel, fontdict = font2)

plt.xlabel(xLabel, fontdict = font2)
plt.ylabel(yLabel, fontdict = font2)
plt.title("Linear Regression Plot, r = " + str(np.around(r, 3)), fontdict = font1)

plt.show()
