# NAME : HASSAN ADNAN
# UCID : 30217418
# QUESTION 1
from string import punctuation


def has_at_least_2_letters(token):

    letter_count = 0
    for ch in token:
        if ch.isalpha():
            letter_count += 1
        if letter_count >= 2:
            return True
    return False


def main():
    filename = "sample-file.txt"
    with open(filename,"r", encoding="utf-8") as f:
        text = f.read()

    raw_tokens = text.split()

    punctuation = ".,!?;:\"'()[]{}<>"

    frequency = {}

    for token in raw_tokens:

        token = token.lower()

        token = token.strip(punctuation)

        if has_at_least_2_letters(token):

            if token in frequency:
                frequency[token] += 1
            else:
                frequency[token] = 1

    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    top_10 = sorted_words[:10]

    for word, count in top_10:
        print(word, count)


if __name__ == "__main__":
    main()




