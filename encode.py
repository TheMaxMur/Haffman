#!/usr/bin/python3
import re
import sys
import bitarray
from haffman import *

G_CODE_H = {}

# Create Haffman dictionary
def create_dict(node, code=''):
    if node:
        if node.left == None and node.right == None:
            G_CODE_H[node.letter] = code
            #print(f"Частота символа %s: %d. Код: %s" % (node.letter, node.weight, code))
        create_dict(node.left, code + '0')
        create_dict(node.right, code + '1')

# Entrypoint
def main(text: str='', path: str=''):
    global G_CODE_H
    G_CODE_H = {}
    #flag = input("Code by symbol or by word? (w/s): ")
    flag = 'w'
    try:
        open(path + "dictionary", 'w')
    except:
        pass
    if flag == 's':
        root = generate(list(text))[0]
    elif flag == 'w':
        text = clear_txt(text).upper()
        massive = text.split()
        tmp = []
        for i in range(len(massive)):
            tmp.append(massive[i])
            if i != len(massive) - 1:
                tmp.append(" ")
        massive = tmp
        del tmp
        root = generate(massive, path)[0]
        del massive
    else:
        print("ERROR")
        return
    create_dict(root)
    G_CODE_H = dict(sorted(G_CODE_H.items(), key=lambda x: len(x[1])))
    '''for el in G_CODE_H.keys():
        if el == '\n':
            print(f"Symbol '\\n'. Code: %s." % G_CODE_H[el])
            continue
        if el == ' ':
            print(f"Symbol '\\s'. Code: %s." % G_CODE_H[el])
            continue
        print(f"Symbol '%s'. Code: %s." % (el, G_CODE_H[el]))'''
    if flag == 's':
        text = encode_text(text, G_CODE_H)
    else:
        text = encode_text_word(text, G_CODE_H)
    #print(f"Encoded text: %s" % text)
    array = bitarray.bitarray(text)
    with open(path + "encoded_text", 'bw') as encode_file:
        array.tofile(encode_file)

def read_file(filename: str):
    if filename:
        try:
            with open(filename, 'r') as data:
                return (data.read())#.replace('\n', ' '))
        except:
            pass

if __name__ == '__main__':
    argv = sys.argv[1:]
    #argv = ["hamlet/original_text", "romeo_and_juliet/original_text", "tempest/original_text", "king_lear/original_text"]
    if "--help" in argv:
        print("USAGE:\n./encode.py /path/to/file/for/encode")
        exit()
    if argv:
        for el in argv:
            text = read_file(el)
            if text:
                main(text, "/".join(el.split("/")[:len(el.split("/")) - 1]) + '/')
            else:
                print("ERROR. Can't read file.")

    else:
        print("USAGE:\n./encode.py /path/to/file/for/encode")
        #main('ababasdbas bbbsafs dflk jsdaasdf')
