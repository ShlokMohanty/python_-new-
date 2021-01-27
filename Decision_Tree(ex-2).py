data = pd.read_csv("D://iris_lyst9272.csv")
data


# In[7]:


data = pd.read_csv("D:\iris_lyst9272 (1).csv")


# In[8]:


data


# In[9]:


import numpy as np
import matplotlib.pyplot as plt


# In[10]:


data['Species'].unique()


# In[11]:


data


# In[12]:


data.Species.value_counts()


# In[13]:


colnames = list(data.columns)


# In[14]:


colnames


# In[15]:


predictors = columns[:4]
target = colnames[4]


# In[16]:


predictors = colnames[:4]
target = colnames[4]


# In[18]:


from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size=0.2)


# In[19]:


train


# In[20]:


test


# In[21]:


from sklearn.tree import DecisionTreeClassifier
help(DecisionTreeClassifier)
model = DecisionTreeClassifier(criterion='entropy')
model.fit(train[predictors],train[target])
sklearn.tree.plot_tree(model)


# In[22]:


import numpy as np
from sklearn.tree import DecisionTreeClassifier
help(DecisionTreeClassifier)
model = DecisionTreeClassifier(criterion="entropy")
model.fit(train[predictors],train[target])
sklearn.tree.plot_tree(model)


# In[23]:


preds = model.predict(test[predictors])
pd.Series(preds).value_counts()


# In[24]:


pd.crosstab(test[target],preds)


# In[25]:


np.mean(preds==test.Species)

