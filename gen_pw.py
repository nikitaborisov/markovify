from markovify import Words

import sys
import math

entropy = float(sys.argv[1])

if len(sys.argv) > 2:
    num_pw = int(sys.argv[2])
else:
    num_pw = 1

if len(sys.argv) > 3:
    wordlist = sys.argv[2]
else:
    wordlist = "/usr/share/dict/words"



with open(wordlist) as words_file:
    word_gen = Words(words_file.read())

# Generate 8 passwords, pick the one you like best
for i in range(num_pw):
    pw = word_gen.gen_pw(entropy+math.log(num_pw,2))
    print(pw)
    
