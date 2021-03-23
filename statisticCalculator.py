import math as mt
import statistics as sts
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt

#loading input file
print("\n","Data Requirements:", "\n",
    "1. Your data should have at least 3 column with the same length", "\n",
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
medianX = np.median(inputX) #medianX = sts.median(inputX)
medianY = np.median(inputY) #medianX = sts.median(inputX)

#mode
modeObjectX = scs.mode(inputX) #modeX = sts.multimode(inputX)
modeX = modeObjectX.mode
modeObjectY = scs.mode(inputY) #modeY = sts.multimode(inputY)
modeY = modeObjectY.mode

#sum
sumX = np.sum(inputX)
sumY = np.sum(inputY)

#XY
inputXY = np.multiply(inputX, inputY)

#sum of XY
sumInputXY = np.sum(inputXY)

#mean
meanX = np.mean(inputX) #meanX = sts.mean(inputX) #meanX = sumX / lengthX
meanY = np.mean(inputY) #meanY = sts.mean(inputY) #meanY = sumY / lengthY

#harmonic mean
hmeanX = scs.hmean(inputX) #hmeanX = sts.harmonic_mean(inputX) #hmeanX = lengthX / sum(1 / item for item in inputX)
hmeanY = scs.hmean(inputY) #hmeanY = sts.harmonic_mean(inputY) #hmeanY = lengthY / sum(1 / item for item in inputY)

#geometric mean
gmeanX = scs.gmean(inputX) #gmeanX = sts.geometric_mean(inputX)
gmeanY = scs.gmean(inputY) #gmeanY = sts.geometric_mean(inputY)

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
varX = np.var(inputX, ddof = 1) #varX = sts.variance(inputX) #varX = (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputX, meanX)))) / (lengthX - 1)
varY = np.var(inputY, ddof = 1) #varY = sts.variance(inputY) #varY = (np.sum(np.multiply(np.subtract(inputY, meanY), np.subtract(inputY, meanY)))) / (lengthY - 1)

#standard deviation
sX = np.std(inputX, ddof = 1) #sX = sts.stdev(inputX) #sX = mt.sqrt(varX)
sY = np.std(inputY, ddof = 1) #sY = sts.stdev(inputY) #sY = mt.sqrt(varY)

#skewness
skX = scs.skew(inputX, bias = False) #skX = (lengthX * (np.multiply(np.multiply(np.subtract(inputX, meanX), np.subtract(inputX, meanX)), np.subtract(inputX, meanX)))) / ((lengthX - 1) * (lengthX - 2) * sX * sX * sX)
skY = scs.skew(inputY, bias = False) #skX = (lengthY * (np.multiply(np.multiply(np.subtract(inputY, meanY), np.subtract(inputX, meanY)), np.subtract(inputY, meanY)))) / ((lengthY - 1) * (lengthY - 2) * sY * sY * sY)

#percentiles 25%, 50%, 75%
perX = np.percentile(inputX, [25, 50, 75]) #perX = sts.quantiles(inputX, n = 4, method = "inclussive")
perY = np.percentile(inputY, [25, 50, 75]) #perY = sts.quantiles(inputY, n = 4, method = "inclussive")

#range
ranX = np.ptp(inputX)
ranY = np.ptp(inputY)

#covariance
covMatrix = np.cov(inputX, inputY) #cov = (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputY, meanY)))) / (lengthX - 1)
cov = covMatrix[0, 1]

#pearson product-moment correlation coefficient
r = scs.pearsonr(inputX, inputY)[0] #r = np.corrcoef(inputX, inputY)[0, 1] #r = (np.subtract((lengthX * sumInputXY), (sumX * sumY))) / (mt.sqrt(((sumSquareX * lengthX) - squareSumX) * ((sumSquareY * lengthY) - squareSumY)))

#spearman correlation coefficient
rho = scs.spearmanr(inputX, inputY)[0]

#kendall correlation coefficient
tau = scs.kendalltau(inputX, inputY)[0]

#determination coefficient
r2 = r * r

#linear regression
"""
b = (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputY, meanY)))) / (np.sum(np.multiply(np.subtract(inputX, meanX), np.subtract(inputX, meanX))))

a = (sumY - (b * sumX)) / lengthX
"""

slope, intercept, r, p, stderr = scs.linregress(inputX, inputY)

b = slope

a = intercept

bEq = ""
aEq = ""

if b == 1 :
    bEq = "X"
elif b == 0 :
    bEq = ""
elif b == -1 :
    bEq = "- X"
else :
    bEq = str(np.around(b, 5)) + "X"

if a > 0 :
    aEq = "+" + " " + str(np.around(a, 5))
elif a == 0 :
    aEq = ""
elif a < 0 :
    aEq = "-" + " " + str(np.around(abs(a), 5))
else :
    aEq = str(np.around(a, 5))

eq = "Y = " + bEq + " " + aEq

#displaying data
print("\n", "The Input X:", "\n", inputX)
print("\n", "The Input Y:", "\n", inputY)
print("\n", "The Length of X:", "\n", lengthX)
print("\n", "The Length of Y:", "\n", lengthY)
print("\n", "The Median of X:", "\n", medianX)
print("\n", "The Median of Y:", "\n", medianY)
print("\n", "The Mode of X:", "\n", modeX, ", occurence: ", modeObjectX.count, "times")
print("\n", "The Mode of Y:", "\n", modeY, ", occurence: ", modeObjectY.count, "times")
print("\n", "The Sum of X:", "\n", sumX)
print("\n", "The Sum of Y:", "\n", sumY)
print("\n", "The XY:", "\n", inputXY)
print("\n", "The Sum of XY:", "\n", sumInputXY)
print("\n", "The Mean of X:", "\n", meanX)
print("\n", "The Mean of Y:", "\n", meanY)
print("\n", "The Harmonic Mean of X:", "\n", hmeanX)
print("\n", "The Harmonic Mean of Y:", "\n", hmeanY)
print("\n", "The Geometric Mean of X:", "\n", gmeanX)
print("\n", "The Geometric Mean of Y:", "\n", gmeanY)
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
print("\n", "The Skewness of X:", "\n", skX)
print("\n", "The Skewness of Y:", "\n", skY)
print("\n", "The Covariance:", "\n", cov)
print("\n", "The Pearson Product-Moment Correlation Coefficient:", "\n", r)
print("\n", "The Spearman Correlation Coefficient:", "\n", rho)
print("\n", "The Kendall Correlation Coefficient:", "\n", tau)
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

plotY = np.add(np.multiply(b, inputX), a)

plt.scatter(inputX, inputY, c = colorbar, cmap = "rainbow")
plt.plot(inputX, plotY, ls = "-", label = eq, color = "#1D1D1D", linewidth = "1")

plt.legend(loc="lower right")

plt.grid()

font1 = {"family":"serif","color":"#1D1D1D","size":20}
font2 = {"family":"serif","color":"#1D1D1D","size":15}

plt.colorbar().ax.set_ylabel(cLabel, fontdict = font2)

plt.xlabel(xLabel, fontdict = font2)
plt.ylabel(yLabel, fontdict = font2)
plt.title("Linear Regression Plot, r = " + str(np.around(r, 3)), fontdict = font1)

plt.show()
