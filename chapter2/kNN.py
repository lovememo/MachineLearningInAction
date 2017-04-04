# -*- coding: utf-8 -*-
from numpy import *
import operator

'''
Created on 2017年4月4日
k-临近算法
@author: lovememo
'''
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()#返回数据排序后的index
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    #排序函数，对classCount进行排序，第一个参数为迭代器，第二个参数可以理解为回调函数
    sortedClassCount = sorted(classCount.iteritems(),
    key=operator.itemgetter(1), reverse=True)
    #返回逆序排序后的顶部元素，并返回其key，即label
    return sortedClassCount[0][0]
    
    
    
group, labels = createDataSet()

print classify0([2,2], group, labels, 2)

# 
# group, labels = createDataSet()
# print group
# print labels
# print group.shape[0]
# inX1 = [0,0]
# newData = tile(inX1, (group.shape[0], 1))
# print newData
