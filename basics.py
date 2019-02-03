#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tags = pd.read_csv("/home/tushar/Downloads/ml-20m/tags.csv",sep=',')


# In[3]:


tags


# In[4]:


tags['parsed_time'] = pd.to_datetime(tags['timestamp'],unit='s')


# In[5]:


tags['parsed_time']


# In[6]:


tags['parsed_time'].dtype


# In[7]:


# select rows according to our need
tags['greater'] = tags['parsed_time'] > '2015-05-01'


# In[8]:


tags['greater'].shape 


# In[9]:


# sorting the values(In ascending order of time stamp)

output = tags.sort_values(by='parsed_time',ascending=True)
output


# In[ ]:





# In[ ]:





# In[ ]:




