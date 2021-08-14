import random
import re

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    '''Word Finder: finds random words from a dictionary.
    >>> wf = WordFinder("words.txt")
    235886 words read
    '''

    def __init__(self, words):
        self.count = 0
        self.words = open(words, 'r').read().splitlines()

        self.countWords()
        # Calling self.random() in doctest will throw error. We're just calling this here to test for a proper response from the random() method.(Should be commented out or deleted for production.)
        # self.random()
        
    def countWords(self):
        for word in self.words:
            self.count += 1
        
        print(str(self.count) + ' words read')

    def random(self):
        print(random.choice(self.words))


class SpecialWordFinder(WordFinder):
    '''Retrieves a random word while removing blank and commented lines.

    words_plus.txt includes comment and blank line (+2 "words" read, normally 235886) for testing purposes with SpecialWordFinder.
    >>> swf = SpecialWordFinder("words_plus.txt")
    235886 words read
    '''

    def __init__(self, words):
        self.clean_file(words)
        super().__init__(words)

    def clean_file(self, words):
        # Adapted from Credit: https://codereview.stackexchange.com/questions/145126/open-a-text-file-and-remove-any-blank-lines
        # https://stackoverflow.com/questions/1706198/python-how-to-ignore-comment-lines-when-reading-in-a-file
        with open(words) as wordsfile:
            lines = wordsfile.readlines()

        with open(words, 'w') as wordsfile:
            # Removes comment lines from words file.
            lines = filter(lambda x: not x.strip().startswith('#'), lines)
            # Removes blank lines from words file
            lines = filter(lambda x: x.strip(), lines)
            # Rewrites to word file
            wordsfile.writelines(lines)



