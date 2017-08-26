# -*- coding: utf-8 -*-
import regression as re
import matplotlib.pyplot as plt

from numpy import *

def testStandRegres():
    xArr, yArr = re.loadDataSet('ex0.txt')
    ws = re.standRegres(xArr, yArr)
    xMat=mat(xArr)
    yMat=mat(yArr)
    fig = plt.figure()
    ax = fig.add_subplot(111) #将画布分成1行1列，将从左到右，从上到下第一块显示图画
    ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0],c='purple',label='realData',marker='.')
    #scatter散点图
    # matrix[a:b,c:d]  第a到b行，且第c到d列 左闭右开
    # matrix[a,b] 第a行，第b列
    xCopy=xMat.copy()
    #xCopy.sort(0)#y轴方向排序
    yHat=xCopy*ws
    ax.plot(xCopy[:,1],yHat,c='green')
    # print yHat.T.flatten().A[0].size
    # print yMat.flatten().A[0].size
    # print yHat
    # print yMat
    correlation = corrcoef(yHat.T, yMat )
    print correlation
    plt.show()

def testGaussWeight():
    xArr, yArr = re.loadDataSet('ex0.txt')
    xMat = mat(xArr)
    #xArr.sort(0)
    xMat.sort(0)
    weights = re.getGaussWeightArr([1,0.5], xMat, 0.4)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xMat[:,1], weights)    
    plt.show()
def main():
    #testStandRegres()
    testGaussWeight()
    print 'end'
main();




