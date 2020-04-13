import re

def check_if_apos_or_letter(words):
    real_words = []
    for word in words:
        real_word = ''
        for letter in word:
            if letter.isalnum():
                real_word += letter
            elif (letter == "'" and word[word.index("'")-1].isalpha() and
                  word[word.index("'")+1].isalpha()):
                real_word += letter
        real_words.append(real_word)

    return real_words

def count_words(sentence):
    punct = "`~!@#$%^&*()_-+=[{]}|;:\\?\">,<./"
    split_sent = re.split('\s|,|_', sentence.lower())
    words = filter(lambda x: x not in punct, split_sent)

    revised_sent = check_if_apos_or_letter(words)
    word_count = {word: 0 for word in revised_sent}

    for key in word_count.keys():
        for word in revised_sent:
            if key == word:
                word_count[key] += 1

    return word_count
