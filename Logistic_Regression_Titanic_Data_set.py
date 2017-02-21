
# coding: utf-8

# In[54]:

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import cufflinks as cf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics  import classification_report
from sklearn.metrics  import confusion_matrix
cf.go_offline()
train = pd.read_csv('titanic_train.csv')
train.head()
# checking the missing values
train.isnull()
sns.heatmap(train.isnull(),yticklabels= False)
plt.show()
sns.countplot(data= train, x= 'Survived', hue= 'Sex' )
plt.show()
sns.countplot(data= train, x= 'Pclass', hue= 'Sex' )
plt.show()
sns.distplot(train['Age'].dropna(), kde = False)
plt.show()
train['Age'].iplot(kind='hist',bins = 30)
df = train[['Pclass','Age']]
fd = pd.pivot_table(df, columns=["Pclass"])
print(fd)
def impute_Age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if (pd.isnull(Age)):
        if Pclass == 1:
             return 38
        elif Pclass == 2:
             return 29
        else:
             return 25
    else:
        return Age

train['Age']= train[['Age','Pclass']].apply(impute_Age, axis = 1)
train.drop('Cabin', axis = 1 , inplace = True)
train.dropna(inplace=True)
sns.heatmap(train.isnull() , yticklabels= False)
plt.show()
sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
train.drop(['PassengerId','Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train = pd.concat([train,sex,embark],axis=1)
train.head()
X= train.drop(['Survived'],axis=1)
y=train['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101) 
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict( X_test)  
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))


# In[ ]:



