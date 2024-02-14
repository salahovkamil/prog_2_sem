import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

# In[3]:


parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('month', type=str, help='Input dir for videos')
parser.add_argument('year', type=str, help='Output dir for image')
args = parser.parse_args()
print(args.month)
print(args.year)
month = args.month
year = args.year
assert isinstance(int(month), int)
assert 13 > int(month) > 0, "number should be > 0 and <= 12"
assert isinstance(int(year), int)
assert int(year) > 0, "number should be > 0"
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
