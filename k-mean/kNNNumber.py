#!/user/bin/env python
# coding=utf-8


from numpy import *
import operator, os


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

def img2vector(filename):
    returnVector = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line = fr.readline()
        for j in range(32):
            returnVector[0, 32 * i + j] = int(line[j])
    return returnVector


def getVec(dir):
    labels = []
    fileList = os.listdir(dir)
    m = len(fileList)
    mat = zeros((m, 1024))
    for i in range(m):
        file = fileList[i]
        fileName = file.split(".")[0]
        numClass = int(fileName.split("_")[0])
        labels.append(numClass)
        mat[i] = img2vector(dir + "/" + file)
    return mat, labels


def handwritingClassTest():
    trainMat, hwLabels = getVec("digits/trainingDigits")
    testMat, testLabel = getVec("digits/testDigits")
    errorCount = 0.0
    mTest = len(testMat)
    for i in range(mTest):
        result = classify0(testMat[i], trainMat, hwLabels, 3)
        print "No.%d, 识别结果为：%s, 正确结果为：%s" % (i, result, testLabel[i])
        if result != testLabel[i]:
            errorCount += 1
    print "总共处理数量：%d，识别错误数：%f, 识别错误率为：%f" % (mTest, errorCount, errorCount/mTest)

handwritingClassTest()