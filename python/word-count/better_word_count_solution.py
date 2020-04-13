import re


def count_words(sentence):
    # re.sub(pattern, repl, string)
    # repl can be a string or a function
    # Returns the string obtained by replacing the leftmost
    # non-overlapping occurrences of pattern in string by repl
    words = re.sub("[^a-z0-9']", ' ', sentence.lower()).split()
    words = [word.strip("'") for word in words]

    return dict((word, words.count(word)) for word in set(words))

print(count_words("''one,two\n\t--three\none_two three-one"))
