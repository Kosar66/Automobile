#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv('Automobile_data.csv')
data.head()


# In[5]:


sns.distplot(data['wheel-base'])


# In[7]:


data['wheel-base'].isnull().sum()


# In[8]:


data.isnull().sum()


# In[28]:


sns.jointplot(data['horsepower'], data['price'] )


# In[20]:


data.corr()


# In[29]:


sns.pairplot(data)


# In[ ]:




