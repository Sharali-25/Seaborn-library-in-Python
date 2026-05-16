import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("USA_Housing.csv")
print(df.head(10))

print(df.info())

print(df.describe())

print(df.columns)

# Creating pairplot

sns.pairplot(df.select_dtypes(include=[np.number]))

# Creating Co-Relation heat map

sns.heatmap(df.select_dtypes(include=[np.number]).corr(),annot=True)

# Displaying the plots

plt.show()