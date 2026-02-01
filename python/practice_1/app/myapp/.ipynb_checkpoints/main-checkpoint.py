#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
print(f'os.getcwd():{os.getcwd()}')


# In[9]:


from class_sample import User


# In[10]:


user = User("tetsutaro", 31, "Tokyo, Japan")


# In[11]:


print(user.name)


# In[12]:


print(user.age)


# In[13]:


user.increment_age()
print(user.age)


# In[14]:


user.start_name()


# In[ ]:





# In[ ]:




