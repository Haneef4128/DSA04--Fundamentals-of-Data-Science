import pandas as pd
df = pd.read_csv("user_interaction.csv")
likes_distribution = df['likes'].value_counts().reset_index()
likes_distribution.columns = ['Likes', 'Frequency']
print("Likes Frequency Distribution:")
print(likes_distribution)
