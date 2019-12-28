#!/usr/bin/env python
# coding: utf-8

# # NumPy Operations
#    - Array with Array
#    - Array with Scalar
#    - Universal Array Functions

# In[1]:


import numpy as np


# In[2]:


ar = np.arange(0,11)


# In[3]:


ar


# In[4]:


#addtion of arrays
ar + ar


# In[5]:


ar + 100


# In[6]:


ar - 100


# In[7]:


ar * 100


# In[8]:


ar / ar


# In[9]:


1 / ar


# In[10]:


#array with its power raised value
ar **2


# In[11]:


#square root of every element in the array
np.sqrt(ar)


# In[12]:


#calculating exponential value
np.exp(ar)


# In[13]:


np.max(ar)


# In[14]:


np.argmax(ar)


# In[15]:


#sin,cosin operations on the array
np.sin(ar)


# In[17]:


#log operations on the array
np.log(ar)


# # link for the universal array functions in numpy : https://docs.scipy.org/doc/numpy/reference/ufuncs.html

# In[ ]:




