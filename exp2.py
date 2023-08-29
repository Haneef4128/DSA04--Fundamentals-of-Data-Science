import numpy as np
import csv
data=[]
with open("sales.csv",'r')as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        data.append(row)
sales=np.array(data[1:],dtype=float)
avg=np.mean(sales)
print("The Average:{:.2f}".format(avg))
