import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
dir(iris)

iris.feature_names()
iris.feature_names
df =  pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()
df['target']=iris.target
iris.target_names
df[df.target==1].head()
df[df.target==2].head()
df['flower_name']= df.target.apply(lambda x: iris.target_names[x])
import matplotlib.pyplot as plt
%matplotlib inline
df0 = df[df.target==0]
df1 = df[df.target==1]
df2 = df[df.target==2]
plt.scatter(df0['sepal length (cm)',df1['sepal width (cm)'],color='green',marker='+')
