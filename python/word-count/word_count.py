# -*- coding: utf-8 -*-

from collections import defaultdict
import re


def word_count(sentence):
    """Works but fails one"""

    result = defaultdict(int)

    words = re.sub("[\W]|_", " ", sentence, re.UNICODE)

    for word in words.lower().split():
        result[word] += 1

    return result
