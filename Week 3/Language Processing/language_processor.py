import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def read_book(book_file_name):
    """Reads a book and returns it as a string"""
    
    # Using the with statement here closes the file automatically!
    with open(book_file_name, "r", encoding = "utf8") as book_file:
        book_text = book_file.read()

    return book_text.replace("\n", "").replace("\r", "")

def count_words(text):
    """Counts the number of times each word occures in a text while skipping punctuation."""
    
    # Turn it into lower case
    text = text.lower()

    # Remove ponctuations
    ponctuations = [".", ",", ";", ":", "'", "\""]

    for char in ponctuations:
        text = text.replace(char, "")

    # This here is a much faster way instead of using the for loop
    return Counter(text.split(" "))

def word_stats(word_counts):
    """Returns the number of unique words and word frequencies"""

    return (len(word_counts), word_counts.values())

english_book_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/Language Processing/Books/English/shakespeare/Romeo and Juliet.txt"
english_book_text = read_book(english_book_file_name)

german_book_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/Language Processing/Books/German/shakespeare/Romeo und Julia.txt"
german_book_text = read_book(german_book_file_name)

(english_num_of_words, english_counts) = word_stats(count_words(english_book_text))
(german_num_of_words, german_counts) = word_stats(count_words(german_book_text))

print(english_num_of_words, sum(english_counts))
print(german_num_of_words, sum(german_counts))

book_directory = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/Language Processing/Books"

stats = pd.DataFrame(columns = ("Language", "Author", "Title", "Length", "UniqueWords"))
title_num = 1

for language in os.listdir(book_directory):

    for author in os.listdir(book_directory + "/" + language):

        for title in os.listdir(book_directory + "/" + language + "/" + author):
            
            book_file_name = book_directory + "/" + language + "/" + author + "/" + title
            book_text = read_book(book_file_name)

            (num_of_words, counts) = word_stats(count_words(book_text))
            
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_of_words
            title_num += 1

print(stats.head())
print(stats.tail())

plt.figure(figsize = (10, 10))

subset = stats[stats.Language == "English"]
plt.loglog(subset.Length, subset.UniqueWords, "o", label = "English", color = "crimson")

subset = stats[stats.Language == "French"]
plt.loglog(subset.Length, subset.UniqueWords, "o", label = "French", color = "green")

subset = stats[stats.Language == "German"]
plt.loglog(subset.Length, subset.UniqueWords, "o", label = "German", color = "orange")

subset = stats[stats.Language == "Portuguese"]
plt.loglog(subset.Length, subset.UniqueWords, "o", label = "Portuguese", color = "blueviolet")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")

plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/Language Processing/statistics.pdf")
plt.show()