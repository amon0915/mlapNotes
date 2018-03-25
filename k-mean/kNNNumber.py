#!/user/bin/env python
# coding=utf-8


from numpy import *
import os
import kNNDating as knn

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
        result = knn.classify0(testMat[i], trainMat, hwLabels, 3)
        print "No.%d, 识别结果为：%s, 正确结果为：%s" % (i, result, testLabel[i])
        if result != testLabel[i]:
            errorCount += 1
    print "总共处理数量：%d，识别错误数：%f, 识别错误率为：%f" % (mTest, errorCount, errorCount/mTest)

if "__main__" == __name__:
    handwritingClassTest()