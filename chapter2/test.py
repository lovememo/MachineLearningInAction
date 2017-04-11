# -*- coding: utf-8 -*-
import kNN
import matplotlib.pyplot as plt
from numpy import *

dataSet,labels = kNN.createDataSet()
k=3
inX=[-1,-1]
result = kNN.classify0(inX, dataSet, labels, 3)
print result


# datingDataMat, datingLabels = kNN.createDatingDataSet(1000)
datingDataMat, datingLabels = kNN.file2matrix("datingTestSet2.txt")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
