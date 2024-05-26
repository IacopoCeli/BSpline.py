from BSpline import *

ctrlp = []
ctrlpFile = open("C:\\Users\\iacop\\Documents\\projects\\Python\\BSpline-v2.0\\ctrlp.txt", "r")
line:str = ctrlpFile.readline()
while(line != ""):
    ctrlp.append(line.strip().split("\t"))
    ctrlp[-1][0] = float(ctrlp[-1][0])
    ctrlp[-1][1] = float(ctrlp[-1][1])
    line = ctrlpFile.readline()
ctrlpFile.close()

knots = []
knotsFile = open("C:\\Users\\iacop\\Documents\\projects\\Python\\BSpline-v2.0\\knots.txt", "r")
line:str = knotsFile.readline()
while(line != ""):
    knots.append(line.strip())
    knots[-1] = float(knots[-1])
    line = knotsFile.readline()
knotsFile.close()

# type: 0 -> Opened ; 1 -> Clamped ; 2 -> Bezier
bs = BSpline(ctrlp, knots, 3)

bs.CalcBSplineShape()

bs.CalcShape(0.25, 10)

resultsFile = open("RESULT.txt", "w")
for ele in bs.Shape:
    resultsFile.write(str(ele[0]) + "\t" + str(ele[1]) + "\n")
resultsFile.close()
