from itertools import groupby
import re


def encode(string):
    return ''.join(map(lambda char: helper(char),
                       [list(g) for k, g in groupby(string)]))


def helper(char):
    return char[0] if len(char) == 1 \
        else str(len(char)) + char[0]


def decode(string):
    groups = re.findall('(\d*\D)', string)
    pairs = map(lambda g: [re.match('\d*', g).group(),
                           g[-1]], groups)

    return ''.join(map(
        lambda x: int(x[0]) * x[1] if x[0].isdigit() else x[1], pairs
    ))
