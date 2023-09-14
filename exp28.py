from sklearn.cluster import KMeans
import numpy as np
def get_user_input():
    feature1 = float(input("Enter shopping feature 1: "))
    feature2 = float(input("Enter shopping feature 2: "))
    return np.array([[feature1, feature2]])
def main():
    X = np.array([[10, 20], [15, 18], [5, 25], [30, 5], [8, 15]]) 
    num_clusters = 3  
    kmeans = KMeans(n_clusters=num_clusters,n_init=10)
    kmeans.fit(X)
    new_customer= get_user_input()
    segment = kmeans.predict(new_customer)
    print(f"The new customer belongs to segment {segment[0]}.")

if __name__ == "__main__":
    main()
