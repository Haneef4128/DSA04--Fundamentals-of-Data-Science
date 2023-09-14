import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
np.random.seed(0)
num_customers = 200
total_amount_spent = np.random.randint(50, 1000, size=num_customers)
num_items_purchased = np.random.randint(1, 30, size=num_customers)
data = pd.DataFrame({
    'TotalAmountSpent': total_amount_spent,
    'NumItemsPurchased': num_items_purchased})
num_clusters = 3  # Number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=0,n_init=10)
cluster_labels = kmeans.fit_predict(data)
data['Cluster'] = cluster_labels

plt.figure(figsize=(8, 6))
for cluster_id in range(num_clusters):
    plt.scatter(
        data[data['Cluster'] == cluster_id]['TotalAmountSpent'],
        data[data['Cluster'] == cluster_id]['NumItemsPurchased'],
        label=f'Cluster {cluster_id}'
    )
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.title('Customer Segmentation using K-Means Clustering')
plt.legend()
plt.show()
