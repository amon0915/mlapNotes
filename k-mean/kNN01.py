#!/user/bin/env python
# coding=utf-8


from numpy import *
import operator


def createDateset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
#
# def runBaseKNN(x, group, label, k):
#     distList = []
#     for i in group:
#         distList.append(sqrt(sum(square(x - i))))
#     labelSort = []
#     for i in range(len(k)):
#         min = 99999
#         for dist in distList:
#             if dist < min

def classify0(inX, dataSet, labels, k):
    # 获取行列数，第一位是行，第二位是列
    dataSetSize = dataSet.shape[0]
    # tile函数，对inX进行行列扩充
    tileRes = tile(inX, (dataSetSize, 1))
    print tileRes
    diffMat = tileRes - dataSet
    print diffMat
    sqDiffMat = diffMat ** 2
    print "sqDiffMat = ", sqDiffMat
    # 矩阵行相加
    sqDistances = sqDiffMat.sum(axis=1)
    print "sqDistances = ", sqDistances
    distances = sqDistances ** 0.5
    print "distance = ", distances
    # 按值升序排序，并返回原始下标
    sortedDis = distances.argsort()
    print "sortedDis = ", sortedDis
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDis[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # sorted是python内置函数：http://www.runoob.com/python/python-func-sorted.html
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "sortedClassCount=", sortedClassCount
    return sortedClassCount

group, label = createDateset();
classify0(array([0.5, 0.6]), group, label, 3)