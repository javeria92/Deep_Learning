#!/usr/bin/env python
# coding: utf-8

# # Data representations for neural networks
# - nd-Array = tensor
# - count number of opening brickets [[[ == number dimension, rank, axis

# # 2.2.1
# Scalars (0D tensors)

# In[3]:


# import numpy as np

a = np.array(25)
print(a)
print(a.ndim)
print(a.shape)

# OD Tesnor, 0 Rank Tensor


# # 2.2.2
# Vectors (1D tensors)

# In[7]:


a = np.array([1,3,4,9,6])
print(a)
print("Dimension",a.ndim)
print("Shape",a.shape)

# 1D Tensor, 1 Rank Tensor, Vector, 1Axes Tensor


# # 2.2.3
# Matrices (2D tensors)

# In[8]:


a = np.array([[5, 78, 2, 34, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])

print(a)
print("Dimension",a.ndim)
print("Shape",a.shape)


# # 2.2.4
# 3D tensors and higher-dimensional tensors

# In[10]:


a = np.arange(1,46).reshape((3,3,5))

print(a)
print("Dimension",a.ndim)
print("Shape",a.shape)


# In[11]:


a = np.ones((2,2,2,2,2))

print(a)
print("Dimension",a.ndim)
print("Shape",a.shape)


# In[ ]:




