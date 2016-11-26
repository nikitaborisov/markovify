import unittest
import markovify
import itertools
import os

class WordTest(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__),
                               "texts/sherlock.txt")) as f:
            self.sherlock = f.read()

    def test_generate_corpus(self):
        input_str = "This is a string.. with some w/ords and\tpun.732ctuation!"
        words = ["this", "is", "a", "string", "with", "some", "w", "ords",
                 "and", "pun", "ctuation"]
        words_list = [list(w) for w in words]
        generated_list = list(markovify.Words.generate_corpus(input_str))
        self.assertEqual(generated_list, words_list)


    def test_words(self):
        word_model = markovify.Words(self.sherlock)

        word = word_model.generate_word(12)
        assert len(word) == 12
        assert all(x.islower() for x in word)

        pw = word_model.gen_pw(40)
        print(pw)

    def test_entropy(self):
        model = { ('___BEGIN__',): {'0': 1.0, '1': 0.0 },
                 ('0',): { '0': 0.5, '1': 0.5 },
                 ('1',): { '0': 1.0, '1': 0. } }
        chain = markovify.Chain(None, state_size=1, model=model, finite=True)

        self.assertAlmostEqual(chain.entropy(('___BEGIN__',)), 0)
        self.assertAlmostEqual(chain.entropy(('0',)), 1.0)
        self.assertAlmostEqual(chain.entropy(('1',)), 0)

        # should have 10 zeros
        pw = chain.gen_entropy(10)
        assert 10 <= len([c for c in pw if c == '0']) <= 11


if __name__ == '__main__':
    unittest.main()
