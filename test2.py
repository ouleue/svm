import random
import random
import numpy as np
from numpy import *
import random

#mutag_list = np.load("data.mutag")  # array of igraph objects

### ALL KERNELS COMPUTE
#K1 = gk.CalculateEdgeHistKernel(mutag_list)
yLabel = [0,0,0,0,1,0]
yPredict = [1,1,1,1,0,1]
yLabel = np.array(yLabel)
yPredict = np.array(yPredict)
#yLabel = np.vstack((yLabel, yPredict))
#yLabel = yLabel + yPredict
#yLabel.extend(yPredict)
a = np.zeros(len(yLabel) + len(yPredict),dtype=int)
a = np.array(a)
print(a)
sum = 0
for i in range(0,len(yLabel)):
    a[sum] = yLabel[i]
    sum = sum + 1
for i in range(0,len(yPredict)):
    a[sum] = yPredict[i]
    sum = sum + 1

print(a)