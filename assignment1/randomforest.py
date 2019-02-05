import pandas as pd
import numpy as np

train = pd.read_csv('adult.data',header= None)



train= np.array(train)
for i in range(len(train)):
    train[i][14] = train[i][14].replace('.','')

tot=train

for i in range(tot.shape[1]):
    temp= list(set(tot[:,i]))
    dic = dict()
    for j in range(len(temp)):
        dic.update({temp[j]:j})
    for j in range(len(train)):
        train[j][i] = dic[train[j][i]]
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

X = train[:,:-1]
Y = train[:,-1]
Y = Y.astype('int')

clf.fit(X,Y)

from sklearn.metrics import accuracy_score

print(accuracy_score(clf.predict(X),Y))
