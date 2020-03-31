#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[12]:


pip install geopy


# In[13]:


from geopy.distance import geodesic
kolkata = (22.5726, 88.3639) 
delhi = (28.7041, 77.1025) 
print(geodesic(kolkata, delhi).km)


# In[ ]:




