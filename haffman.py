import re

# Binary tree struct
class Node():
    def __init__(self, letter: str, weight: int, left=None, right=None):
        self.letter = letter
        self.weight = weight
        self.left = left
        self.right = right

# Sort dictionary by value
def sort_dict(d: dict):
    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get)

    for w in sorted_keys:
        sorted_dict[w] = d[w]
    return (sorted_dict)

# Generate dictionary by frequency
def generate_dict(text: list=[]):
    result = {}
    for let in text:
        if let not in list(result.keys()):
            result[let] = 1
        else:
            result[let] += 1
    return (result)

# Generate massive objects 
def generate_first_lvl_tree(d: dict):
    massive = []
    for key in d.keys():
        massive.append(Node(key, d[key]))
    return (massive)

# Create binary tree lvl
def generate_tree(m: list):
    massive = []
    letter = m[0].letter + m[1].letter
    weight = m[0].weight + m[1].weight
    left = m[0]
    right = m[1]
    massive.append(Node(letter, weight, left, right))
    for i in range(2, len(m)):
        massive.append(m[i])
    massive.sort(key=lambda x: x.weight)
    return (massive)

# Generate binary tree
def generate(text: list=[]):
    result = sort_dict(generate_dict(text))
    with open("dictionary", 'a') as table:
        for el in result.keys():
            table.write(f"'%s' : %s\n" % (el, result[el]))
    massive = generate_first_lvl_tree(result)
    while (len(massive) > 1):
        massive = generate_tree(massive)
    return (massive)

# Generate binary tree for decode
def generate_for_decode(result: dict={}):
    massive = generate_first_lvl_tree(result)
    while (len(massive) > 1):
        massive = generate_tree(massive)
    return (massive)

# Encode text by Haffman code
def encode_text(text: str='', code_h: dict={}):
    res = ""
    while text:
        for k in code_h:
            if text.startswith(k):
                res += code_h[k]
                text = text[len(k):]
    #text = re.sub(' ', '', text)
    return (res)

# Decode text by Haffman code
def decode_text(text: str='', dictionary: dict={}):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(dictionary[k]):
                res += k
                text = text[len(dictionary[k]):]
    return (res)

def encode_text_word(text: str='', dictionary: dict={}):
    massive = text.split()
    result = []
    for i in range(len(massive)):
        result.append(dictionary[massive[i]])
        if i != len(massive) - 1:
            result.append(dictionary[" "])
    massive = ''
    for el in result:
        massive += el
    return (massive)

def clear_txt(text: str=''):
    text = re.sub(r"[^A-Za-z0-9А-Яа-я\s]", "", text)
    #text = re.sub(r"\n", "", text)
    return (text)

