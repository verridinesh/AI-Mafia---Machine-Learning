#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


get_ipython().system('pip3 install numpy')


# In[4]:


##I am going to learn numpy now!


# # I am going to learn numpy now!
# 

# # This is a new headline

# In[5]:


import numpy as np


# In[6]:


arr = np.array([[1,2,3],
               [4,2,3]])


# In[7]:


type(arr)


# In[8]:


arr.ndim


# In[9]:


arr.shape


# In[10]:


arr = np.array([1,2,3])


# In[11]:


arr.shape


# In[12]:


arr.size


# In[13]:


print(np.__version__)
np.show_config()


# In[14]:


Z = np.zeros(10)
print(Z)


# In[15]:


Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))


# In[16]:


Z = np.zeros(10)
Z[4] = 1
print(Z)


# In[17]:


Z = np.arange(50)
Z = Z[::-1]
print(Z)


# In[18]:


Z = np.arange(9).reshape(3,3)
print(Z)


# In[19]:


np.ones((3,4))


# In[20]:


np.eye(3)


# In[21]:


get_ipython().run_line_magic('pinfo', 'np.arange')


# In[22]:


get_ipython().run_line_magic('pinfo', 'np.eye')


# In[23]:


f = np.arange(0,30,5)


# In[24]:


print(f)


# In[27]:


g = np.linspace(0,5,10)
print(g)


# In[28]:


arr = np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])


# In[29]:


arr


# In[30]:


arr[1::2, :3:2]


# # BASIC OPERATIONS

# In[31]:


a = np.array([1,2,3,4,5])


# In[32]:


a+1


# In[33]:


arr = np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])


# In[34]:


arr.T


# In[37]:


print(arr.max())


# In[36]:





# In[ ]:




