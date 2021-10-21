#!/usr/bin/python3
from haffman import *
import re
import sys

G_CODE_H = {}

# Create Haffman dictionary
def create_dict(node, code: str=""):
    if node:
        if node.left == None and node.right == None:
            G_CODE_H[node.letter] = code
            #print(f"Частота символа %s: %d. Код: %s" % (node.letter, node.weight, code))
        create_dict(node.left, code + '0')
        create_dict(node.right, code + '1')

# Entrypoint
def main(d_file: str="", encode_file: str=""):
    global G_CODE_H
    with open(d_file, 'r') as data:
        for line in data:
            line = line.strip()
            sym = re.sub(r"\'", "" , line.split(" : ")[0])
            weigth = line.split(" : ")[1]
            G_CODE_H[sym] = int(weigth)
    root = generate_for_decode(G_CODE_H)[0]
    G_CODE_H = {}
    create_dict(root)
    text = open(encode_file, "r").read().strip()
    text = decode_text(text, G_CODE_H)
    with open("decode", 'w') as encode_file:
        encode_file.write(f"%s\n" % text)


if __name__ == '__main__':
    #argv = sys.argv[1:]
    main("dictionary", "encode")
