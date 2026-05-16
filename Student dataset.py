import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Student.csv")
print(df.head(10))

print(df.info())

print(df.describe())

print(df.shape)

print(df.isnull().sum())

#plt.plot(df["StudyTimeWeekly"],df["GPA"])
#plt.title("Study Time VS GPA")
#plt.xlabel("Study Time")
#plt.ylabel("GPA")

#plt.show()

gender_GPA = df.groupby("Gender")["GPA"].mean()
plt.bar(gender_GPA.index, gender_GPA.values)
plt.title("Average GPA by gender")
plt.xlabel("Gender")
plt.ylabel("Average GPA")
plt.show()