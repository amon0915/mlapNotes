#!/user/bin/env python
# coding=utf-8


import math

def createDataSet():
    dataSet = [
        [1,1,"yes"],
        [1,1,"yes"],
        [1,0,'no'],
        [0,1,'no'],
        [0,1,'no'],
    ]
    label = ['不上浮呼吸','脚蹼']
    return dataSet, label


def calEnt(dataSet):
    num = len(dataSet)
    labelCount = {}
    ent = 0.0
    for vec in dataSet:
        label = vec[-1]
        if label not in labelCount.keys():
            labelCount[label] = 0
        labelCount[label] += 1
    for key in labelCount.keys():
        prop = float(labelCount[key]) / num
        ent -= prop * math.log(prop, 2)
    return ent

def splitClassSet(dataSet, axis, value):
    resultList = []
    for vec in dataSet:
        if vec[axis] != value:
            continue
        e = []
        for i in range(len(vec)):
            e.append(vec[i])
        resultList.append(e)
    return resultList

# ID3算法，获取最大增益，利用max(总熵-条件熵)对应的分类
def id3(dataSet):
    totalEnt = calEnt(dataSet)
    bestFeature = -1
    bestEntGain = 0.0
    featureNum = len(dataSet[0]) - 1
    for i in range(featureNum):
        print "维度：%d" % i
        featrueValList = [item[i] for item in dataSet]
        uniqueVals = set(featrueValList)
        newEnt = 0.0
        # 计算条件熵
        for v in uniqueVals:
            subDataSet = splitClassSet(dataSet, i, v)
            prop = float(len(subDataSet)) / len(dataSet)
            print subDataSet, prop * calEnt(subDataSet)
            newEnt += prop * calEnt(subDataSet)
        # 获取最大增益以及对应的feature
        print "条件熵：%f" % newEnt
        if bestEntGain < totalEnt - newEnt:
            bestEntGain = totalEnt - newEnt
            bestFeature = i
    return bestFeature


if __name__ == "__main__":
    dataSet, labels = createDataSet()
    # print calEnt(dataSet);
    # print splitClassSet(dataSet, 0, 0)
    # print splitClassSet(dataSet, 0, 1)
    # print splitClassSet(dataSet, 1, 0)
    # print splitClassSet(dataSet, 1, 1)
    print id3(dataSet)
