#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
df = pd.read_csv("D:\company_salaries.csv")


# In[ ]:





# In[4]:


df.head()


# In[5]:


inputs = df.drop("salary_more_than_100k",axis="columns")
target = df['salary_more_than_100k']


# In[6]:


inputs


# In[7]:


target


# In[10]:


from sklearn.preprocessing import LabelEncoder


# In[11]:


le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()


# In[12]:


inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['company_n'] = le_company.fit_transform(inputs['company'])


# In[ ]:




