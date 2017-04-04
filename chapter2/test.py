import kNN
import matplotlib
import matplotlib.pyplot as plt

dataSet,labels = kNN.createDataSet()
k=3
inX=[-1,-1]
result = kNN.classify0(inX, dataSet, labels, 3)
print result
datingDataMat, datingLabels = kNN.createDatingDataSet(1000)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
plt.show()
