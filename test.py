import random
import numpy as np

x = [[1,3,5],[2,34,5],[3,2,4],[4,34,5],[5,2,4]]
z = [1,2,3,4,5]
y = [[11,22,33],[44,55,66]]
u = [1,1]
#print(x)
#random.shuffle(x)
#print(x)
c = np.array(x)
d = np.array(y)
#y = c[:,2]
#c1 = np.array(y)
#print(c)
#print(y)

# print(z)
# print(u)
# print(z+u)


y.append(x[0])
print(y)

#y = np.array(y)
t = np.insert(x, 3, values=z, axis=1)
#t4 = np.concatenate((c,y),axis=1)
#print(np.c_[x,y])
# print(x[2])
#
# for i in range(0,len(y))[::-1]:
#     print(i)

#print(t)
#print(np.insert(x, len(x), values=y, axis=0))
#print(c[2:])

#print(c[:,2])#获取第3列数据

#c1 = np.delete(c, -1, axis=1)#删除最后一行
#print(c1)

#x = [[1,3,5],[2,34,5],[3,2,4],[4,34,5],[5,2,4]]
#z = [1,2,3,4,5]
#y = [11,22,33]
print(c)
#print(c[0,1])

print(c.shape[1])

all4 = np.zeros([2, c.shape[1]],dtype=int)
all5 = np.zeros([3, 3],dtype=int)
print(all4)

n = 0
m = 0
for i in range(0,len(c)):
    if(c[i,2] == 4):
        #all4 = np.append(c[i])
        #all4 = np.insert(all4, n, values=c[i], axis=0)
        for j in range(0, 3):
            all4[n,j] = c[i,j]
        n = n + 1
    else:
        for j in range(0, 3):
            all5[m,j] = c[i,j]
        m = m + 1


print(all4)
print(all5)


# a = np.empty([0, 3])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# c = [[7, 8, 9]]
#
# print(a.shape)
# print(b.shape)
#
# a = np.append(a, b, axis=0)
#
# a = np.append(a, c, axis=0)
#
# print(a.shape)
# print(b.shape)

def qselect(ary_list, k):
    if len(ary_list) < k:
        return ary_list

    tmp = ary_list[0]
    left = [x for x in ary_list[1:] if x <= tmp] + [tmp]
    llen = len(left)
    if llen == k:
        return left
    if llen > k:
        return qselect(left, k)
    else:
        right = [x for x in ary_list[1:] if x > tmp]
        return left + qselect(right, k-llen)
    pass

#a = [10.899284, 2.89732894, 38.78233, 9.89723, 22.897238, 53.6752312, 47.78632423, 7.89734273, 3.6534624, 97.76524983]
a = np.zeros(4,dtype=float)
print(a)
a[0] = 10.899284
a[1] = 2.89732894
a[2] = 38.78233
a[3] = 9.89723

b = qselect(a, 2)
print(b)
a[0] = 0
print(a[0])

e = np.vstack((c,d))
print(e)

for i in range(0, len(e))[::-1]:
    if (e[i,0] == 11):
        e = np.delete(e, i, axis=0)
print(e)