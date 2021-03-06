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

def createDatingDataSet(rows):
    retData = random.rand(rows, 3)
    retData = retData * 10
    for i in range(len(retData)):
        rowData = retData[i]
        for j in range(len(rowData)):
            rowData[j] = round(rowData[j], 4)    
    labels = random.rand(rows)
    for i in range(len(labels)):
        labels[i] = int(100*labels[i]) % 3 + 1
    return retData, labels

def file2matrix(filename):                         
    fr = open(filename)
    #打开文件，按行读入
    arrayOLines = fr.readlines()    
    #获得文件行数 
    numberOfLines = len(arrayOLines)  
    #创建m行n列的零矩阵 
    returnMat = zeros((numberOfLines,3))          
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        #删除行前面的空格
        listFromLine = line.split('\t')
         #根据分隔符划分
        returnMat[index,:] = listFromLine[0:3]
        #取得每一行的内容存起来
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

#归一化数据集（将数据等比例缩放至0~1之间的值）
def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    rangeValue = maxValue - minValue
    rowNum = dataSet.shape[0];
    retSet = dataSet - tile(minValue, (rowNum, 1))
    retSet = retSet / rangeValue
    return retSet, rangeValue, minValue

dataSet = random.rand(100,3)
retSet,rangeValue,minValue = autoNorm(dataSet)
print retSet
print rangeValue
print minValue
# print dataSet
 

    
    
# group, labels = createDataSet()
# 
# print classify0([2,2], group, labels, 2)

# 
# group, labels = createDataSet()
# print group
# print labels
# print group.shape[0]
# inX1 = [0,0]
# newData = tile(inX1, (group.shape[0], 1))
# print newData
