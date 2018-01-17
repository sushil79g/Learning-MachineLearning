
# coding: utf-8
#Simple implementation of Linear Regression of line y=m*x+c
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.random.randint(0,20,size=10)
y= np.random.randint(0,20,size=10)

n=np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)


sxy = np.sum(y*x-n*y_mean*x_mean)
sxx = np.sum(x**2-n*x_mean*x_mean)


m = sxy/sxx
c = y_mean - m*x_mean 


plt.scatter(x,y,color='m',marker='o')
y_predict= m*x+c
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# print(y-y_pred)
plt.plot(x,y_predict,color='g')
plt.show()


# In[ ]:



