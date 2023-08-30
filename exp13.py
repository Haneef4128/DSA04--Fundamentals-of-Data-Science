import string
def process_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return words

def calculate_frequency(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def display_frequency_distribution(word_freq):
    print("Word Frequency Distribution:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    with open("sales.csv", "r") as file:
        text = file.read()
    words = process_text(text)
    word_freq = calculate_frequency(words)
    display_frequency_distribution(word_freq)
