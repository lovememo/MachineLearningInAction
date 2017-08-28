# -*- coding: utf-8 -*-
from numpy import *

def standRegres(xArr,yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T #行向量转列向量
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0: #计算行列式
        print "This matrix is singular, cannot do inverse" #奇异矩阵不可逆
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

#Locally Weighted Linear Regression LWLR （局部加权线性回归）
#返回局部回归系数.
def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    weights = getGaussWeightMat(testPoint, xArr, k)
    xTx = xMat.T * (weights * xMat)#根据矩阵乘法结合律，这里没有括号也是可以的，加括号易于理解
    if linalg.det(xTx) == 0:
        print "This matrix is singular, cannot do inverse" #奇异矩阵不可逆
        return
    ws = xTx.I * xMat.T * (weights * yMat)
    return ws

def getGaussWeightMat(fixedPoint, inputPoints, k=1):
    m = shape(inputPoints)[0]#对样本数据的每一个元素进行加权，所以权重对角矩阵的长度肯定是样本数据个数
    gaussWeightMat = mat(eye(m))#权重对角矩阵 参看numpy.eye
    fixedPoint = mat(fixedPoint)
    inputPoints = mat(inputPoints)
    for i in range(m):
        diffMat =  fixedPoint - inputPoints[i,:]
        gaussWeightMat[i,i] = exp(diffMat * diffMat.T / (-2 * k ** 2))
    return gaussWeightMat

def getGaussWeightArr(fixedPoint, inputPoints, k=1):
    gaussWeightMat = getGaussWeightMat(fixedPoint, inputPoints, k)
    m = shape(gaussWeightMat)[0]
    gaussWeightArr = []
    for i in range(m):
        gaussWeightArr.append(gaussWeightMat[i,i])
    return gaussWeightArr
    
    

#testArr为行向量数组
def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        ws = lwlr(testArr[i], xArr, yArr, k)
        yHat[i] = testArr[i] * ws
    return yHat
        

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t') #strip -> trim
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1])) # -1 -> last element
    return dataMat,labelMat

def rssErr(yArr, yHat):
    diffMat = mat(yArr) - mat(yHat)
    return diffMat * diffMat.T





