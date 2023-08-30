import pandas as pd
df = pd.read_csv("review.csv")
customer_review = df['comments'].value_counts().reset_index()
customer_review.columns = ['Comments', 'Frequency']
print("Review Frequency Distribution:")
print(customer_review)
