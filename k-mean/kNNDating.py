#!/user/bin/env python
# coding=utf-8


from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import operator


def file2matrix(filename):
    fr = open(filename)
    arrayLine = fr.readlines()
    numberOfLines = len(arrayLine)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayLine:
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def classify0(inX, dataSet, labels, k):
    # 获取行列数，第一位是行，第二位是列
    dataSetSize = dataSet.shape[0]
    # tile函数，对inX进行行列扩充
    tileRes = tile(inX, (dataSetSize, 1))
    # print tileRes
    diffMat = tileRes - dataSet
    # print diffMat
    sqDiffMat = diffMat ** 2
    # print "sqDiffMat = ", sqDiffMat
    # 矩阵行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # print "sqDistances = ", sqDistances
    distances = sqDistances ** 0.5
    # print "distance = ", distances
    # 按值升序排序，并返回原始下标
    sortedDis = distances.argsort()
    # print "sortedDis = ", sortedDis
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDis[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # sorted是python内置函数：http://www.runoob.com/python/python-func-sorted.html
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    # print "sortedClassCount=", sortedClassCount
    return sortedClassCount[0][0]


def showFigure():
    returnMat, classLabelVector = file2matrix("datingTestSet2.txt")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(returnMat[:, 0], returnMat[:, 1], 10.0 * array(classLabelVector), 1000.0 * array(classLabelVector))
    plt.show()


def autoNorm(dataSet):
    # 获取列的最大最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals

    # 获取dataSet行数
    m = shape(dataSet)[0]
    # 对行复制扩充
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    print "normDataSet=", normDataSet
    return normDataSet, ranges, minVals


def datingClassTest(hoRatio, k):
    returnMat, datingLabels = file2matrix("datingTestSet2.txt")
    normDateSet, ranges, minVals = autoNorm(returnMat)
    totalLine = normDateSet.shape[0]
    choseLine = int(normDateSet.shape[0] * hoRatio)
    errorCount = 0
    for i in range(choseLine):
        cResult = classify0(normDateSet[i, :], normDateSet[choseLine:totalLine, :], datingLabels[choseLine:totalLine],
                            k)
        realResult = datingLabels[i]
        print "算法分类结果为：%s， 实际结果为：%s" % (cResult, realResult)
        if cResult != realResult:
            errorCount += 1
    print "errorCount=%s, 错误率率为：%f" % (errorCount, errorCount/float(choseLine))


# datingClassTest(0.1, 4)

def chosePerson():
    choseSet = ['不喜欢','一般般','很喜欢']
    mile = float(raw_input("飞行里程："))
    iceCream = float(raw_input("每年吃多少升冰淇淋："))
    gamePer = float(raw_input("每天游戏时间占比："))
    returnMat, datingLabels = file2matrix("datingTestSet2.txt")
    normDateSet, ranges, minVals = autoNorm(returnMat)
    # 归一化输入数据
    inputArray = array([mile, gamePer, iceCream])
    inX = (inputArray - minVals) / ranges

    cResult = classify0(inX, normDateSet, datingLabels, 3);
    print "cResult = ", cResult
    print choseSet[cResult - 1]


# chosePerson();
showFigure();