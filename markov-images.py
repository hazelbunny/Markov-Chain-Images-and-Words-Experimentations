import numpy
import json
from random import choice
file = open("dataset.json",mode='r')
_dataset=json.load(file)
dataset=json.loads(_dataset)
     
data=[]

dencode = "RGBL"
x,y=0,0

prev=[0,0,0,0]
column=[]
for x in range(0,500):
    for y in range(0,500):
        values=choice(dataset[x][y])
        _next=[]
        list_values=[]
        for i in range(0,4):
            list_values.append(prev[i]+values[i][dencode[i]])
            _next.append(abs(values[i][dencode[i]]))
        column.append(list_values)
        prev=_next
    data.append(column)
    column=[]
from matplotlib import pyplot as plt
plt.imshow(data, interpolation='nearest')
plt.axis("off")
plt.grid(False)
plt.show()
