#!/usr/bin/env python
# coding: utf-8

# In[8]:


type(1)


# In[9]:


type(3.14)


# In[10]:


type("Big Data")


# In[11]:


type('bigdata')


# In[12]:


type(True)


# In[13]:


type(False)


# In[14]:


type([1,2,"intruder",3])


# In[15]:


for x in range(100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    if x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
    else :
        print(x)


# In[16]:


Dev3_5 = [x for x in range (1000) if x % 5 == 0 or x % 3 == 0]
sum(Dev3_5)


# In[ ]:




