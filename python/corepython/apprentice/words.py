#!/usr/bin/env python3
from urllib.request import urlopen

URL = "http://sixty-north.com/c/t.txt"


# fetch list of worlds and return as list
def fetch_words():
    with urlopen(URL) as story:
        story_words = []
        for line in story:
            words = line.decode("UTF-8").split()
            for word in words:
                story_words.append(word)

    return story_words


# print the list of words
def print_items(items):
    for item in items:
        print(item)


def main():
    words = fetch_words()
    print_items(words)


if __name__ == "__main__":
    main()
