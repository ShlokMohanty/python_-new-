import pandas as pd
df=pd.read_csv("D:/train_and_test2.csv")
df.head()
df.drop(['Fare','Pclass','Embarked'],axis='columns',inplace=True)
df.head()
