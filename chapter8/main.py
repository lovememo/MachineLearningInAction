# -*- coding: utf-8 -*-
import regression as re
import matplotlib.pyplot as plt

from numpy import *


def testStandRegres():
    xArr, yArr = re.loadDataSet('ex0.txt')
    ws = re.standRegres(xArr, yArr)
    xMat = mat(xArr)
    yMat = mat(yArr)
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 将画布分成1行1列，将从左到右，从上到下第一块显示图画
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten(
    ).A[0], c='purple', label='realData', marker='.')
    # scatter散点图
    # matrix[a:b,c:d]  第a到b行，且第c到d列 左闭右开
    # matrix[a,b] 第a行，第b列
    xCopy = xMat.copy()
    # xCopy.sort(0)#y轴方向排序
    yHat = xCopy * ws
    ax.plot(xCopy[:, 1], yHat, c='green')
    # print yHat.T.flatten().A[0].size
    # print yMat.flatten().A[0].size
    # print yHat
    # print yMat
    correlation = corrcoef(yHat.T, yMat)
    print correlation
    plt.show()


def testGaussWeight():
    xArr, yArr = re.loadDataSet('ex0.txt')
    xMat = mat(xArr)
    yMat = mat(yArr)

    fig = plt.figure()
    ax = fig.add_subplot(411)  # 将画布分成1行1列，将从左到右，从上到下第一块显示图画
    plt.yticks(linspace(2.5, 5, 6))
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten(
    ).A[0], c='purple', label='realData', marker='.')

    xMat.sort(0)
    weights = re.getGaussWeightArr([1, 0.5], xMat, 0.5)
    ax = fig.add_subplot(412)
    plt.yticks(linspace(0.6, 1, 9))
    ax.plot(xMat[:, 1], weights)
    plt.text(0.7, 0.75, r'$k=0.5$')

    weights = re.getGaussWeightArr([1, 0.5], xMat, 0.1)
    ax = fig.add_subplot(413)
    plt.yticks(linspace(0, 1, 6))
    ax.plot(xMat[:, 1], weights)
    plt.text(0.7, 0.5, r'$k=0.1$')

    weights = re.getGaussWeightArr([1, 0.5], xMat, 0.01)
    ax = fig.add_subplot(414)
    plt.yticks(linspace(0, 1, 6))
    ax.plot(xMat[:, 1], weights, label='k=0.01')
    plt.text(0.7, 0.5, r'$k=0.01$')
    plt.show()


def testLwlr():
    xArr, yArr = re.loadDataSet('ex0.txt')
    xMat = mat(xArr)
    yMat = mat(yArr)

    fig = plt.figure()
    ax = fig.add_subplot(311)  # 将画布分成1行1列，将从左到右，从上到下第一块显示图画
    privateShow(ax, xMat, yMat, 1.0)

    ax = fig.add_subplot(312)
    privateShow(ax, xMat, yMat, 0.02)

    ax = fig.add_subplot(313)
    privateShow(ax, xMat, yMat, 0.002)
    plt.show()


def privateShow(ax, xMat, yMat, k):
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten(
    ).A[0], c='purple', label='realData', marker='.')
    ind = xMat[:, 1].argsort(0)  # 获取按第一列排序后的索引
    newXmat = xMat[ind][:, 0, :]  # 按索引排序后会升一个维度，所以降一个维度
    newYmat = yMat.T[ind][:, 0, :].T
    yHat = re.lwlrTest(newXmat, newXmat.A, newYmat.A, k)
    ax.plot(newXmat[:, 1], yHat, c='green')


def calcErr(xArr, yArr, sIdx, eIdx, k, testStartIdx, testEndIdx, ws):
    yHat = re.lwlrTest(xArr[testStartIdx:testEndIdx],
                       xArr[sIdx:eIdx], yArr[sIdx:eIdx], k)
    print ('k=%f: %f'%(k,re.rssErr(yArr[testStartIdx:testEndIdx], yHat)))
    print ('标准： %f'%(re.rssErr(yArr[testStartIdx:testEndIdx], (mat(xArr[testStartIdx:testEndIdx])*ws).T)))


#预测鲍鱼年龄
def testAbalone():
    xArr, yArr = re.loadDataSet('abalone.txt')
    ws = re.standRegres(xArr, yArr)
    print ws
    for k in [2,10]:
        calcErr(xArr, yArr, 0, 299, k, 300, 350, ws)
        calcErr(xArr, yArr, 0, 299, k, 350, 400, ws)
        calcErr(xArr, yArr, 0, 299, k, 400, 450, ws)
        calcErr(xArr, yArr, 0, 299, k, 450, 500, ws)
        calcErr(xArr, yArr, 0, 299, k, 500, 600, ws)
        print ''
    


def main():
    #testStandRegres()
    #testGaussWeight()
    #testLwlr();
    testAbalone()
    print 'end'


main()
