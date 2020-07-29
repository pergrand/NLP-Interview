# -*- coding: utf-8 -*-
# @Time : 2020/7/29 13:48
# @Author : lowe.li
# @Site : 
# @File : MP.py
# @Software : PyCharm

import numpy  as np
import matplotlib  as mpl
import matplotlib.pyplot as plt

#定义坐标,设定6组输入数据，每组为（x0,x1,x2）
X=np.array([[1,4,3],
            [1,5,4],
            [1,4,5],
            [1,1,1],
            [1,2,1],
            [1,3,2]]);

#设定输入向量的期待输出值
Y=np.array([1,1,1,-1,-1,-1]);

#设定权值向量(w0,w1,w2),权值范围为-1,1
W = (np.random.random(3)-0.5)*2;
#设定学习率
lr = 0.3;
#计算迭代次数
n=0;
#神经网络输出
O=0;

def  update():
    global  X,Y,W,lr,n;
    n=n+1;
    O=np.sign(np.dot(X,W.T));
    #计算权值差
    W_Tmp = lr*((Y-O.T).dot(X));
    W = W+W_Tmp;


if __name__ == '__main__':
    for index in range (100):
        update()

        O=np.sign(np.dot(X,W.T))
#         print(O)
#         print(Y)
        if(O == Y).all():
            print('Finished')
            print('epoch:',n)
            break
x1=[3,4]
y1=[3,3]
x2=[1]
y2=[1]

k=-W[1]/W[2]
d=-W[0]/W[2]
print('k=',k)
print('d=',d)
xdata=np.linspace(0,5)
plt.figure()
plt.plot(xdata,xdata*k+d,'r')
plt.plot(x1,y1,'bo')
plt.plot(x2,y2,'yo')
plt.show()