import base64
import itertools
from Crypto.Util.strxor import strxor_c


def break_single_xor(data):
    freqs = {
        "a": 8.167,
        "b": 1.492,
        "c": 2.782,
        "d": 4.253,
        "e": 12.702,
        "f": 2.228,
        "g": 2.015,
        "h": 6.094,
        "i": 6.966,
        "j": 0.153,
        "k": 0.772,
        "l": 4.025,
        "m": 2.406,
        "n": 6.749,
        "o": 7.507,
        "p": 1.929,
        "q": 0.095,
        "r": 5.987,
        "s": 6.327,
        "t": 9.056,
        "u": 2.758,
        "v": 0.978,
        "w": 2.360,
        "x": 0.150,
        "y": 1.974,
        "z": 0.074,
        " ": 20.0
    }

    def score(s):
        score = 0
        for i in s:
            i = i.lower()
            if i in freqs:
                score += freqs[i]
        return score

    def key(p):
        return score(p[1])

    return max([(i, strxor_c(data, i)) for i in range(0, 256)], key=key)


def break_repeat_xor(data, length):
    blocks = [data[i:i+length] for i in range(0, len(data), length)]
    transposedBlocks = list(itertools.izip_longest(*blocks, fillvalue=0))
    key = [break_single_xor(bytes(x))[0] for x in transposedBlocks]
    return key


def get_hamming_distance(x, y):
    return sum([bin(ord(x[i]) ^ ord(y[i])).count('1') for i in range(len(x))])


def get_edit_distance(data, k):
    blocks = [data[i:i+k] for i in range(0, len(data), k)][0:4]
    pairs = list(itertools.combinations(blocks, 2))
    scores = [get_hamming_distance(p[0], p[1])/float(k) for p in pairs][0:6]
    return sum(scores) / len(scores)

data = base64.b64decode(open('6.txt', 'r').read())

k = min(range(2, 41), key=lambda k: get_edit_distance(data, k))
print k
print break_repeat_xor(data, 29)
