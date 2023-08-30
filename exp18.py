import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
data={
"age":[23, 57, 58, 58, 60, 61],
"fat":[9, 26, 7, 17, 31, 25]
}
df=pd.DataFrame(data)
print(df)
print("Mean age",np.mean(data['age']))
print("Mean fat",np.mean(data['fat']))
print("Median age",np.median(data['age']))
print("Median fat",np.median(data['fat']))
print("Standard deviation age",np.std(data['age']))
print("Standard deviation fat",np.std(data['fat']))
plt.boxplot(df)
plt.show()
plt.scatter(data['age'],data['fat'])
plt.show()
sm.qqplot(df)   
plt.show()

  
