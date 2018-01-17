
# coding: utf-8

# In[18]:

#Simple implementation of Linear Regression of line y=m*x+c
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[40]:

x = np.random.randint(0,20,size=10)
y= np.random.randint(0,20,size=10)


# In[20]:

n=np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)


# In[21]:

sxy = np.sum(y*x-n*y_mean*x_mean)


# In[22]:

sxx = np.sum(x**2-n*x_mean*x_mean)


# In[23]:

m = sxy/sxx
c = y_mean - m*x_mean 


# In[41]:

plt.scatter(x,y,color='m',marker='o')
y_pred= m*x+c
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# print(y-y_pred)
plt.plot(x,y_pred,color='g')
plt.show()


# In[ ]:



