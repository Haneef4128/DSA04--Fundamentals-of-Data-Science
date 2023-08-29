import numpy as np
import pandas as pd
sales_data=[]
for i in range(1,5):
    sales=np.array(int(input(f"Enter quater{i} data=")))
    sales_data.append(sales)
total=np.sum(sales_data)
four=sales_data[3]
first=sales_data[0]
percentage=((four-first)/first)*100
print("Total:",total)
print("Percentage:",round(percentage))
