import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sports.csv", encoding='latin-1')
average_age = data['Age'].mean()
above_average_age_players = data[data['Age'] > average_age]['Name']
position_counts = data['Position'].value_counts()
plt.bar(position_counts.index, position_counts.values)
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.title('Distribution of Players Based on Positions')
plt.xticks(rotation=45)
plt.show()

print("Top 5 Goal Scorers:")
print(data.nlargest(5, 'Goals'))
print("\nTop 5 Highest Salaries:")
print(data.nlargest(5, 'Salary'))
print(f"\nAverage Age of Players: {average_age:.2f}")
print("\nPlayers Above Average Age:")
print(above_average_age_players)
