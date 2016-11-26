import re
import markovify
import itertools

class Words(object):
    def __init__(self, input_text, state_size = 2, finite=False):
        runs = self.generate_corpus(input_text)

        self.chain = markovify.Chain(list(runs), state_size, finite=finite)

    @classmethod
    def generate_corpus(self, text):
        for word in re.split(r'(?:\W|\d|_)+', text):
            if word:    # skip empty strings
                yield list(word.lower())

    def generate_word(self, length, start=None):
        return ''.join(itertools.islice(self.chain.gen(start), length))

    def gen_pw(self, entropy):
        return ''.join(self.chain.gen_entropy(entropy))
