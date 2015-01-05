# -*- coding: utf-8 -*-

import random

from .generalwords import WORD_LIST

def get_word(language='en_US', word_list=WORD_LIST):
    """Returns a random word selected from the word list.

    Alternative languages are not currently supported.
    """
    return random.choice(word_list)


def get_words(n=1, language='en_US', word_list=WORD_LIST):
    """Returns a tuple of n words selected from the list."""
    return tuple(get_word(language, word_list) for i in range(n))
