import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("D:/company_salaries.csv")
data.head()
data['Species'].unique()
data.Species.vlaue_counts()
colnames = list(data.columns)
predictors = colnames[:4]
target = colnames[4]
from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size=0.2)
from sklearn.tree import DecisionTreeClassifier
help(DecisionTreeClassifier)
model = DecisionTreeClassifier(criterion='entropy')
model.fit(train[predictors],train[target])
sklearn.tree.plot(model)
