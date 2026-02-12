# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 2

from string import punctuation

def has_atleast_2_letters(token):
    letter_count = 0
    for char in token:
        if ch.isalpha():
            letter_count += 1
        if letter_count >= 2:
           return True
    return False

def main():
    file = "sample.txt"
    with open(file,"r", encoding="utf-8") as f:
        text = f.read()

    raw_tokens = text.split()
    clean_tokens = []

    for token in raw_tokens:
        token = token.lower()
        token = token.strip(punctuation)

        if has_atleast_2_letters(token):
            clean_tokens.append(token)


    bigram_frequency = {}

    for i in range (len(clean_tokens)-1 ) :
        word_1 = clean_tokens[i]
        word_2 = clean_tokens[i+1]

        bigram = (word_1, word_2)

        if bigram in bigram_frequency:
            bigram_frequency[bigram] += 1
        else:
            bigram_frequency[bigram] = 1


    sorted_bigram = sorted(bigram_frequency.items(), key=lambda x: x[1], reverse=True)

    top_5 = sorted_bigram[:5]

    for (word_1, word_2), count in top_5 :
        print(word_1, word_2, count)
