from random import shuffle
import pandas as pd
import numpy as np

#Importing the dataset
dataset = pd.read_csv("Fresher's 19.csv")
dataset.drop(['Branch-S', 'Branch-J'],axis=1, inplace=True)
dataset

#First List of People
x = dataset.iloc[:,0:2]
x.dropna(inplace=True)
x

#Second List of People
y = dataset.iloc[:,2:4]
y

#Imputing the empty entires
senior = [tuple(i) for i in x.values]
junior = [tuple(i) for i in y.values]

x1=[]
x2=[]
k=0
for i in senior:
    if i[1] == 'Male':
        x1.append(senior[k])
        k=k+1
    else:
        x2.append(senior[k])
        k=k+1

y1=[]
y2=[]
for i in junior:
    if i[1] == 'Male':
        y1.append(junior[k])
        k=k+1
    else:
        y2.append(junior[k])
        k=k+1