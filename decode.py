#!/usr/bin/python3
from haffman import *
import re
import sys
import bitarray

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
def main(d_file: str="", encode_file: str="", path: str=""):
    global G_CODE_H
    G_CODE_H = {}
    with open(d_file, 'r') as data:
        for line in data:
            line = line.rstrip("\n")
            sym, weigth = line.split(":")
            #sym = re.sub(r"\'", "" , line.split(" : ")[0])
            #weigth = line.split(" : ")[1]
            G_CODE_H[sym] = hex_to_int(weigth) #int(weigth)
    root = generate_for_decode(G_CODE_H)[0]
    G_CODE_H = {}
    create_dict(root)
    text = bitarray.bitarray()
    with open(encode_file, 'br') as encoded_file:
        text.fromfile(encoded_file)
    result = ""
    for el in text: 
        result += str(el)
    text = result
    del result
    text = decode_text(text, G_CODE_H)
    with open(path + "decoded_text", 'w') as encode_file:
        encode_file.write(f"%s\n" % text)


if __name__ == '__main__':
    argv = sys.argv[1:]
    if "--help" in argv:
        print("USAGE:\n./decode.py path/to/dictionary path/to/encoded_text")
        exit()
    #print("/".join(argv[0].split("/")))
    try:
        main(argv[0], argv[1], "/".join(argv[0].split("/")[:len(argv[0].split("/")) - 1]) + '/')
    except Exception as error:
        print("USAGE:\n./decode.py path/to/dictionary path/to/encoded_text")
    #main("hamlet/dictionary", "hamlet/encoded_text", "hamlet/")
    #main("romeo_and_juliet/dictionary", "romeo_and_juliet/encoded_text", "romeo_and_juliet/")
    #main("romeo_and_juliet/dictionary", "hamlet/encoded_text", "cross-ent/1")
    #main("hamlet/dictionary", "romeo_and_juliet/encoded_text", "cross-ent/2")

