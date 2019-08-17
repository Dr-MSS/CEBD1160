#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


import os
os.getcwd()
os.chdir('C:\\Users\heist\Desktop\python_files')


# In[5]:


df = pd.read_csv('train_titanic.csv')
df.head()


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.head(3)


# In[12]:


df.drop(1,0)


# In[13]:


df.drop('Embarked',1)


# In[14]:


df.dropna(axis = 1, how ='all', inplace = True)


# In[20]:


plt.figure(figsize=(8, 7))
sns.distplot(df['Fare'], hist=True, color='b', bins=50 , hist_kws={'alpha': 0.5});


# In[21]:


plt.figure(figsize=(9, 8))
sns.distplot(df['Survived'], hist=True, color='g', bins=50 , hist_kws={'alpha': 0.4});


# In[22]:


list(set(df.dtypes.tolist()))


# In[23]:


del df['PassengerId']
df_num = df.select_dtypes(include = ['float64', 'int64'])
df_num.head()


# In[24]:


plt.matshow(df.corr())
plt.show()


# In[25]:


sns.pairplot(df)


# In[26]:


df['doubledFare'] = df['Fare']*2
df.head()


# In[27]:


x = df['Age'].mean()
df['Age'].fillna(value=x, inplace=True)


# In[28]:


plt.scatter(df['Age'], df['Fare'])
plt.title('Age Vs Fare plot')


# In[29]:


gb_Survived = df.groupby('Survived')
gb_Survived.count() 


# In[30]:


gb_Survived.mean()


# In[31]:


gb_Survived.std() 


# In[32]:



df_num = df.select_dtypes(include = ['float64', 'int64']) 

df_num_corr = df_num.corr(method = 'kendall')['Survived'][2:]  
golden_features_list = df_num_corr[abs(df_num_corr) > 0.1].sort_values(ascending=False)
print("There are {} correlated values with Survived:\n{}".format(len(golden_features_list), golden_features_list))


# In[ ]:




