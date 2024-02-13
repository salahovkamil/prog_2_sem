#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


month = "02"
year = "2024"
outcome_data = pd.read_excel(f"/home/salahovkamil/outcome_{month}.{year}.xlsx")
outcome_data


# In[8]:


outcome_data["День"] = [int(x.split()[0]) for x in outcome_data["Дата"]]
outcome_data


# In[9]:


fig, ax = plt.subplots(constrained_layout=True)
sns.lineplot(
    data=outcome_data,
    x="День",
    y="Сумма",
    hue="Категория",
    ax=ax
)
ax.legend()
plt.show()


# In[13]:


fig, ax = plt.subplots(constrained_layout=True)
sns.barplot(
    data=outcome_data,
    x="Сумма",
    y="Категория",
    orient = "h",
    estimator="sum",
    errorbar=None,
    ax=ax
)
plt.title(f'{month}.{year}')
plt.show()


# In[ ]:




