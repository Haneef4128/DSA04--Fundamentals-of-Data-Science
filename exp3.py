import pandas as pd
import numpy as np
import csv
data=pd.read_csv('house_data1.csv')
house=np.array(data)
house=house.astype(int)
Bedrooms=house[:,0]
four=house[Bedrooms>4]
avg=np.mean(four[:,2])
print("average of price greater than 4 bedrooms:",avg)
