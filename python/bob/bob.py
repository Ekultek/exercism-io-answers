#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    sentence = SentenceThinker(what)
    if sentence.is_silence():
        return "Fine. Be that way!"
    elif sentence.is_yelling():
        return "Whoa, chill out!"
    elif sentence.is_question():
        return "Sure."
    else:
        return "Whatever."


class SentenceThinker(object):

    def __init__(self, sentence):
        self.sentence = sentence

    def is_yelling(self):
        return self.sentence == self.sentence.upper()

    def is_question(self):
        return self.sentence.endswith("?")

    def is_silence(self):
        return not self.sentence
