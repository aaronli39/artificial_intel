#!/usr/bin/python3

import sys

def do(inp, out, data):
    # vars to use
    alpha = "abcdefghijklmnopqrstuvwxyz"
    words = {}
    writeStuff = ""
    search = []
    
    # open file and make input as list
    try:
        with open(inp, "rU") as inFile:
            search = inFile.read().split("\n")
    except:
        print("error reading input file")
        return

    # create the dictionary of 4 letter words
    for i in data:
        ind = 0
        neighbors = set()
        while ind < 4:
            for letter in alpha:
                word = i[:ind] + letter + i[ind + 1:]
                if word in data and word != i:
                    neighbors.add(word)
            ind += 1

        words[i] = list(neighbors)
    
    # create write data
    if search[0] == "":
        print("input file empty")
        return
    
    for word in search:
        if not words.get(word):
            writeStuff += word + ",0\n"
        else:
            writeStuff += word + "," + str(len(words.get(word))) + "\n"

    # write to file        
    try:
        with open(out, "w") as write:
            write.write(writeStuff)
    except:
        print("error writing file")
        return

def main():
    try:
        with open("dictall.txt", "rU") as temp:
            data = set()
            # create set of all 4 letter words to pass on
            data = {word for word in temp.read().split("\n") if len(word) == 4}
    except:
        print("error while opening file.")

    do(sys.argv[1], sys.argv[2], data)
    # do("inp.txt", "out.txt", data)
    # do(data)

main()