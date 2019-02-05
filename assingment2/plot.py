import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
data = pd.read_csv('winequality-red.csv',sep=';')
temp = []
for i in range(len(data)):
    if data['quality'].iloc[i]<=5:
        temp.append('Low')
    else:
        temp.append('High')
data['class'] = temp
temp = list(data.keys())
temp.remove('quality')
data = data[temp]

def _3plot(a1,a2,a3):

 a = []
 b = []
 c = []
 A = []
 B = []
 C = []

 for i in range(len(data)):
  if data['class'].iloc[i]== 'Low':
   a.append(data[a1].iloc[i])
   b.append(data[a2].iloc[i])
   c.append(data[a3].iloc[i])
  else:
   A.append(data[a1].iloc[i])
   B.append(data[a2].iloc[i])
   C.append(data[a3].iloc[i])


 #plt.hist(A,color='blue')
 #plt.hist(a,color='red')
 #plt.show()

 #plt.hist(B,color='blue')
 #plt.hist(b,color='red')
 #plt.show()

 #plt.hist(B,color='blue')
 #plt.hist(b,color='red')
 #plt.show()

 plt.scatter(a,b,c = 'red')
 plt.scatter(A,B,c = 'blue')
 plt.show()

 plt.scatter(b,c,c = 'red')
 plt.scatter(B,C,c = 'blue')
 plt.show()

 plt.scatter(a,c,c = 'red')
 plt.scatter(A,C,c = 'blue')
 plt.show()

 points = 1000
 fig = plt.figure()
 ax = fig.add_subplot(111, projection='3d')
 ax.scatter(a[:points],b[:points],c[:points],c = 'red')
 ax.scatter(A[:points],B[:points],C[:points],c = 'blue')

 plt.show()

_3plot('total sulfur dioxide','volatile acidity','alcohol')
