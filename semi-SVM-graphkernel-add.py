import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn import metrics
from sklearn import svm
from sklearn import datasets
from sklearn.semi_supervised import LabelPropagation
from sklearn.semi_supervised import label_propagation

def load_data():
    '''
    加载数据集
    '''
    #digits = datasets.load_digits()
    ######   混洗样本　########
    #rng = np.random.RandomState(0)
    #indices = np.arange(len(digits.data))  # 样本下标集合
    #rng.shuffle(indices)  # 混洗样本下标集合
    #X = digits.data[indices] #所有数据
    #y = digits.target[indices] #所有标记
    all = []
    random.shuffle(all)
    all = np.array(all)
    #print(all)
    yAll = all[:, 108]
    print(yAll)
    XAll = np.delete(all, 108, axis=1)  # 删除最后一列
    print(XAll)
    X = XAll[:39]  # 取得总数据的前39行
    XPredict = XAll[39:]  # 获得后26条数据
    y = yAll[:39]  # 取得前39行的标记
    yTrue = yAll[39:]  # 获取后26条数据的标记
    print(len(y))

    #混洗样本,再次混洗，可不加
    #X = np.insert(X, 108, values=y, axis=1)
    #random.shuffle(X)
    #X = np.array(X)
    #y = X[:, 108]
    #print(y)
    #X = np.delete(X, 108, axis=1)  # 删除最后一列

    ###### 生成未标记样本的下标集合 ####
    # 只有 40% 的样本有标记
    #n_labeled_points = 16
    XLabel = X[:16] #获取前16条数据为标记数据
    yLabel = y[:16] #获取前16条数据的标记
    #print(n_labeled_points)
    # 后面 60% 的样本未标记
    #unlabeled_indices = np.arange(len(y))[n_labeled_points:]
    XUnlabel = X[16:] #将后23条数据作为未标记数据
    #print(unlabeled_indices)
    return XLabel, yLabel, XUnlabel, XPredict, yTrue


def semi_predict(*data):
    XLabel, yLabel, XPredict, yTrue = data
    clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf.fit(XLabel, yLabel)
    yPredict = clf.predict(XPredict)
    print("Accuracy:%f" % metrics.accuracy_score(yTrue, yPredict))

# 半监督学习semi-SVM
def test_semi_SVM(*data):
    '''
    测试 LabelPropagation 的用法
    '''
    XLabel, yLabel, XUnlabel, XPredict, yTrue = data
    #print("get ytrue")
    #print(yTrue)
    XAllLabel = np.insert(XLabel, 108, values=yLabel, axis=1)
    random.shuffle(XAllLabel)
    XAllLabel = np.array(XAllLabel)
    yLabel = XAllLabel[:, 108]
    #print(yAll)
    XLabel = np.delete(XAllLabel, 108, axis=1)  # 删除最后一列

    # 必须拷贝，后面要用到 y
    XTrain1 = XLabel
    XTrain2 = XLabel[:round(len(XLabel)/2 + 0.5)] #将训练数据对半分
    XTrain3 = XLabel[round(len(XLabel)/2 + 0.5):]

    yTrain1 = yLabel
    yTrain2 = yLabel[:round(len(XLabel)/2 + 0.5)] #将训练数据标记对半分
    yTrain3 = yLabel[round(len(XLabel)/2 + 0.5):]

    clf1 = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf1.fit(XTrain1, yTrain1)
    yPredSVM1 = clf1.predict(XUnlabel)
    clf2 = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf2.fit(XTrain2, yTrain2)
    yPredSVM2 = clf2.predict(XUnlabel)
    clf3 = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf3.fit(XTrain3, yTrain3)
    yPredSVM3 = clf3.predict(XUnlabel)
    count = 0;
    for i in range(0,len(yPredSVM1))[::-1]:
        if(yPredSVM1[i] == yPredSVM2[i]):
            if(yPredSVM1[i] == yPredSVM3[i]):
                XLabel = np.insert(XLabel, len(XLabel), values=XUnlabel[i], axis=0) #将三个相等的训练数据放到
                yLabel = np.insert(yLabel, len(yLabel), values=yPredSVM1[i], axis=0)
                XUnlabel = np.delete(XUnlabel, i, axis=0)  # 删除第i行
            else:
                count = count + 1
        else:
            count = count + 1
    data1 = XLabel, yLabel, XPredict, yTrue
    data2 = XLabel, yLabel, XUnlabel, XPredict, yTrue
    if(count == 0):
        semi_predict(*data1)
    else:
        if(count == len(yPredSVM1)):
            semi_predict(*data1)
        else:
            test_semi_SVM(*data2)



    ### 获取预测准确率
    # 预测标记
    #predicted_labels = clf.predict(XPredict)
    #print(XPredict)
    #predicted_labels = clf.transduction_[unlabeled_indices]
    # 真实标记
    #yTrue
    #true_labels = y[unlabeled_indices]
    #print("Accuracy:%f" % metrics.accuracy_score(yTrue, predicted_labels))
    # 或者 print("Accuracy:%f"%clf.score(X[unlabeled_indices],true_labels))


# 获取半监督分类数据集
data = load_data()
# 调用 test_LabelPropagation
test_semi_SVM(*data)