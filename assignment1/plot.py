import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
x = pd.read_csv('adult.data',header=None)

def _3plot(a1,a2,a3):

 a = []
 b = []
 c = []
 A = []
 B = []
 C = []

 for i in range(len(x)):
  if x[14].iloc[i]== ' >50K':
   a.append(x[a1].iloc[i])
   b.append(x[a2].iloc[i])
   c.append(x[a3].iloc[i])
  else:
   A.append(x[a1].iloc[i])
   B.append(x[a2].iloc[i])
   C.append(x[a3].iloc[i])


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

_3plot(0,4,10)
