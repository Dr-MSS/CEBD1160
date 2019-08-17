#!/usr/bin/env python
# coding: utf-8

# In[2]:


def remove_dup(list1):
    list2=[]
    for num1 in list1:
        if num1 not in list2:
            list2.append(num1)

    print('The Original list',list1)
    print('The list minus all the duplicates',list2)

list_input=[1,3,3,1,3,5,7,8,1,2,3,1,4,5,4,5,6,8,7,9,6,5,5,7,8,6,4,8,9,5,6,4,3,3,3,9,4,4,5,8,5,9,3]
remove_dup(list_input)


# In[1]:


def remove_dupv2(list1):
    return(list(set(list1)))

list_input=[1,3,3,1,3,5,7,8,1,2,3,1,4,5,4,5,6,8,7,9,6,5,5,7,8,6,4,8,9,5,6,4,3,3,3,9,4,4,5,8,5,9,3]
remove_dupv2(list_input)


# In[11]:


list1=[10,20,30,40,50,60,70,80,90]
def finder (list1,sample):
    for x in list1:
        if x == sample:
            return True
    return False
print(finder(list1,25))
print(finder(list1,30))
print(finder(list1,35))
print(finder(list1,40))


# In[13]:


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([i for i in a if i%2==0])


# In[ ]:




