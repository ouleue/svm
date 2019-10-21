import random
import numpy as np
from numpy import *
import random

#读取数据函数,返回list类型的训练数据集和测试数据集
def loadData(fileName):
    trainingData=[]
    testData=[]
    with open(fileName) as txtData:
        lines=txtData.readlines()
    for line in lines:
        lineData=line.strip().split(',') #去除空白和逗号“,”
        if random.random()<0.7:  #数据集分割比例
            trainingData.append(lineData) #训练数据集
        else:
            testData.append(lineData) #测试数据集
    return trainingData,testData
#输入数据为list类型,分割数据集，分割为特征和标签两部分，返回数据为np.narray类型
def splitData(dataSet):
    character=[]
    label=[]
    for i in range(len(dataSet)):
        character.append([float(tk) for tk in dataSet[i][:-1]])
    label.append(dataSet[i][-1])
    return array(character),array(label)























