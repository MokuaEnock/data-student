import re
import string

ARTICLE_FILE_NAME = "news_article.txt"


def read_article(file_path):
    """Read a text file into a string."""
    with open(file_path, "r", encoding="utf-8") as article_file:
        return article_file.read()


def count_specific_word(text, target_word):
    """Count occurrences of target_word in text."""
    words = text.split()
    target_word_clean = target_word.strip(string.punctuation).lower()

    occurrence_count = 0
    index = 0

    while index < len(words):
        cleaned_word = words[index].strip(string.punctuation).lower()
        if cleaned_word == target_word_clean:
            occurrence_count += 1
        index += 1

    return occurrence_count


def identify_most_common_word(text):
    """Return the most common word in text, or None if there are none."""
    all_words = re.findall(r"[A-Za-z']+", text.lower())

    word_frequencies = {}
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

    return max(word_frequencies, key=word_frequencies.get)


def calculate_average_word_length(text):
    """Return the average word length in text, excluding punctuation."""
    raw_words = re.findall(r"[A-Za-z']+", text)

    total_length = 0
    valid_word_count = 0

    for raw_word in raw_words:
        cleaned_word = raw_word.strip("'")
        if len(cleaned_word) > 0:
            total_length += len(cleaned_word)
            valid_word_count += 1

    if valid_word_count == 0:
        return 0

    return round(total_length / valid_word_count, 2)


def count_paragraphs(text):
    """Count paragraphs, defined as blocks separated by blank lines."""
    paragraphs = re.split(r"\n\s*\n", text)
    return len(paragraphs)


def count_sentences(text):
    """Count sentences, defined as segments ending in . ! or ?"""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return len(sentences)


def get_word_to_search():
    """Prompt the user for a non-empty word to search for."""
    user_word = ""

    while user_word.strip() == "":
        user_word = input("Enter a word to search for in the article: ")
        if user_word.strip() == "":
            print("Input cannot be empty. Please try again.\n")

    return user_word.strip()


def describe_word_length(average_length):
    """Describe average word length as short, moderate, or long."""
    if average_length < 4:
        return "short on average"
    elif average_length < 6:
        return "of moderate length on average"
    else:
        return "long on average"


def main():
    print("=" * 60)
    print("NEWS ARTICLE TEXT ANALYSIS")
    print("=" * 60)

    article_text = read_article(ARTICLE_FILE_NAME)

    target_word = get_word_to_search()
    word_count = count_specific_word(article_text, target_word)
    print(f"\nThe word '{target_word}' appears {word_count} time(s).")

    if word_count == 0:
        print("That word does not appear in this article.")
    elif word_count == 1:
        print("That word appears exactly once.")
    else:
        print("That word appears multiple times.")

    most_common_word = identify_most_common_word(article_text)
    print(f"\nThe most common word is '{most_common_word}'.")

    average_length = calculate_average_word_length(article_text)
    print(f"\nAverage word length: {average_length} "
          f"({describe_word_length(average_length)}).")

    print(f"\nParagraph count: {count_paragraphs(article_text)}")
    print(f"Sentence count: {count_sentences(article_text)}")

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
