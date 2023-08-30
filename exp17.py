import numpy as np
import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
data = pd.read_csv('customer_data.csv')
def preprocess_text(text):
    if isinstance(text, float) and np.isnan(text):
        return [] 
    text = str(text).lower()  
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator) 
    words = text.split()
    stop_words = set(['the', 'and', 'is', 'of', 'to', 'in',
                     'it', ' that', 'you']) 
    words = [word for word in words if word not in stop_words]
    return words
data['processed_feedback'] = data['feedback'].apply(preprocess_text)
all_words = [word for words in data['processed_feedback'] for word in words]
word_freq = Counter(all_words)
N = int(input("Enter the number of top words to display: "))
top_words = word_freq.most_common(N)

for word, freq in top_words:
    print(f"{word}: {freq}")
top_words, freq = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(top_words, freq)
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
