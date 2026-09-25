"""
pythonAssessment.py

Summative Lab: Analyze a News Article

A text analysis program/module that performs the following tasks on a
piece of text (e.g. a news article):
    1. Counts how many times a specific word appears in the text.
    2. Identifies the most common word in the text.
    3. Calculates the average length of the words in the text.
    4. Counts the number of paragraphs in the text.
    5. Counts the number of sentences in the text.

Each analysis task is implemented as its own, independently testable
function. main() ties them together into an interactive program that
reads a news article from a text file and reports the results.

Author: Enock Mokua
"""

import re
import string

ARTICLE_FILE_NAME = "news_article.txt"


def read_article(file_path):
    """
    Read the contents of a news article text file into a string.

    Args:
        file_path (str): Path to the text file containing the article.

    Returns:
        str: The full text of the article.
    """
    with open(file_path, "r", encoding="utf-8") as article_file:
        article_text = article_file.read()
    return article_text


def count_specific_word(text, target_word):
    """
    Count how many times a specific word occurs in the text using a
    case-insensitive word match (punctuation stripped from each word
    before comparing).

    A while loop walks through the list of words in the text one at a
    time, comparing each cleaned word against the target word.

    Args:
        text (str): The text to search.
        target_word (str): The word to count occurrences of.

    Returns:
        int: The number of times target_word appears in text.
    """
    words = text.split()
    target_word_clean = target_word.strip(string.punctuation).lower()

    occurrence_count = 0
    index = 0

    # While loop required to walk through every word in the text
    while index < len(words):
        cleaned_word = words[index].strip(string.punctuation).lower()

        if cleaned_word == target_word_clean:
            occurrence_count += 1

        index += 1

    return occurrence_count


def identify_most_common_word(text):
    """
    Identify the most common word in the text.

    A regular expression extracts alphabetic word tokens (ignoring
    punctuation, numbers, and special characters), and a for loop
    builds a frequency count for each word.

    Args:
        text (str): The text to analyze.

    Returns:
        str or None: The most common word, or None if the text
        contains no words.
    """
    word_pattern = r"[A-Za-z']+"
    all_words = re.findall(word_pattern, text.lower())

    word_frequencies = {}

    # For loop required to tally the frequency of each word
    for word in all_words:
        cleaned_word = word.strip("'")

        if not cleaned_word:
            continue

        if cleaned_word in word_frequencies:
            word_frequencies[cleaned_word] += 1
        else:
            word_frequencies[cleaned_word] = 1

    if not word_frequencies:
        return None

    most_common_word = max(word_frequencies, key=word_frequencies.get)
    return most_common_word


def calculate_average_word_length(text):
    """
    Calculate the average length of the words in the text, excluding
    punctuation and special characters from each word before measuring it.

    Args:
        text (str): The text to analyze.

    Returns:
        float or int: The average word length (0 if there are no words).
    """
    word_pattern = r"[A-Za-z']+"
    raw_words = re.findall(word_pattern, text)

    total_length = 0
    valid_word_count = 0

    for raw_word in raw_words:
        cleaned_word = raw_word.strip("'")

        # Conditional value: only count words that still have letters
        # left after punctuation/special characters are stripped
        if len(cleaned_word) > 0:
            total_length += len(cleaned_word)
            valid_word_count += 1

    if valid_word_count == 0:
        return 0

    average_length = total_length / valid_word_count
    return round(average_length, 2)


def count_paragraphs(text):
    """
    Count the number of paragraphs in the text. Paragraphs are defined
    as blocks of text separated by one or more empty lines.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of paragraphs found.
    """
    # Splitting on blank-line boundaries; an empty string yields a
    # single (empty) paragraph, matching how a blank document is
    # still considered one block of text.
    paragraphs = re.split(r"\n\s*\n", text)
    return len(paragraphs)


def count_sentences(text):
    """
    Count the number of sentences in the text. Sentences are defined
    as text segments ending in '.', '!', or '?'.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of sentences found.
    """
    # Split right after any sentence-ending punctuation followed by
    # whitespace. An empty string yields a single (empty) segment.
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return len(sentences)


def get_word_to_search():
    """
    Prompt the user for a word to search for in the article, validating
    that the input is not empty using a while loop.

    Returns:
        str: A valid, non-empty word supplied by the user.
    """
    user_word = ""

    # While loop required to keep prompting until valid input is given
    while user_word.strip() == "":
        user_word = input(
            "Enter a word you would like to search for in the article: "
        )

        if user_word.strip() == "":
            print("Input cannot be empty. Please try again.\n")

    return user_word.strip()


def describe_word_length(average_length):
    """
    Return a short, human-readable description of the average word
    length using conditional (if/elif/else) logic.

    Args:
        average_length (float): The average word length.

    Returns:
        str: A short description of the average word length.
    """
    if average_length < 4:
        return "short on average"
    elif average_length < 6:
        return "of moderate length on average"
    else:
        return "long on average"


def main():
    """
    Main driver function: reads the article, runs each analysis task,
    and displays the results to the user.
    """
    print("=" * 60)
    print("NEWS ARTICLE TEXT ANALYSIS")
    print("=" * 60)

    article_text = read_article(ARTICLE_FILE_NAME)

    # --- Task 1: Count occurrences of a specific word ---
    target_word = get_word_to_search()
    word_count = count_specific_word(article_text, target_word)

    print(f"\nThe word '{target_word}' appears {word_count} time(s) "
          f"in the article.")

    if word_count == 0:
        print("That word does not appear in this article.")
    elif word_count == 1:
        print("That word appears exactly once.")
    else:
        print("That word appears multiple times.")

    # --- Task 2: Identify the most common word ---
    most_common_word = identify_most_common_word(article_text)
    print(f"\nThe most common word in the article is '{most_common_word}'.")

    # --- Task 3: Calculate average word length ---
    average_length = calculate_average_word_length(article_text)
    length_description = describe_word_length(average_length)
    print(f"\nThe average word length in the article is "
          f"{average_length} characters ({length_description}).")

    # --- Task 4: Count paragraphs ---
    paragraph_count = count_paragraphs(article_text)
    print(f"\nThe article contains {paragraph_count} paragraph(s).")

    # --- Task 5: Count sentences ---
    sentence_count = count_sentences(article_text)
    print(f"\nThe article contains {sentence_count} sentence(s).")

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
