#coding: utf-8

'''
@author:    com0716
@file:      kNN.py
@time:      2017/08/28 19:45:51
'''
from numpy import *
import operator

import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1],
                  [1.0, 1.0],
                  [0.0, 0.0],
                  [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()

    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLine = fr.readlines()
    numberOfLines = len(arrayOLine)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLine:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        #classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


if __name__ == "__main__":
    '''
    group,labels = createDataSet()
    print classify0([0, 0], group, labels, 3)   
    '''
    datingDataMat, datingLabels = file2matrix("datingTestSet.txt")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
    plt.show()
