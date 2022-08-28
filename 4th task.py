import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
data = pd.read_csv('4th data.csv')
# print(data.info())
# print(data.corr())
sns.pairplot(data)
data = pd.get_dummies(data,drop_first=True)
sns.heatmap(data.corr(),annot = True)
# plt.show(block = True)
data.to_csv('concancated_data.csv')
print(data.info())


























