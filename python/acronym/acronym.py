import re


def abbreviate(words):
    filtered = list(filter(None, re.sub(
        '[^a-z\'\s]', ' ', words.lower()).split(' ')))
    return ''.join([word[0].upper() for word in filtered])
