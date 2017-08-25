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




