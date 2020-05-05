#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("battles.csv")


# In[5]:


data.head()


# In[6]:


data_backup = data.copy()


# In[7]:


data.location.unique()


# In[41]:


data_regions = data.region.value_counts()
data_regions = pd.DataFrame(data_regions)
data_regions.head()
data_regions = data_regions.reset_index()


# In[42]:


data_regions.plot(kind="bar")


# In[56]:


bp = sns.barplot(x = 'index', y = 'region', data = data_regions )
plt.xticks(rotation = 45)
bp.set(xlabel = 'Region', ylabel = 'Number of Battles', title = 'Most Violent Region')


# In[67]:


sub_data = data[['region', 'major_death']]
sub_data = sub_data[sub_data['major_death'] >= 1]
sub_data.head(30)


# In[70]:


data_deaths = pd.DataFrame(sub_data.region.value_counts())
data_deaths = data_deaths.reset_index()
data_deaths.head()


# In[72]:


bp2 = sns.barplot(x = 'index', y = 'region', data = data_deaths )
plt.xticks(rotation = 45)
bp2.set(xlabel = 'Region', ylabel = 'Number of Major Deaths', title = 'Regions With Most Significant Character Deaths')


# In[ ]:




