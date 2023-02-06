#!/usr/bin/env python
# coding: utf-8

# In[6]:


def maximumWealth(accounts) -> int:
    output=[]
    for nums in accounts:
        output.append(sum(nums))
    return(max(output))
accounts = [[1,2,3],[7,2,1]]
print(maximumWealth(accounts))


# In[ ]:




