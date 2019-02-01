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
senior=[]
for i in x:
    s = (x.iloc[:, 0:1],x.iloc[:,1:1])
    senior.append(s)

senior

shuffle(x)
x