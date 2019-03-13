#!/usr/bin/python3

import sys

def do(inp, out, data):
    # vars to use
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    words = {}
    writeStuff = ""

    # open file and make input as list
    try:
        with open(inp, "rU") as inFile:
            search = inFile.read().split("\n")
    except:
        print("error reading input file")

    # create the dictionary of 4 letter words
    for i in data:
        ind = 0
        neighbors = set()
        while ind < 4:
            for letter in alpha:
                word = i[:ind] + letter + i[ind + 1:]
                if word in data and word not in search:
                    neighbors.add(word)
            ind += 1

        words[i] = list(neighbors)
    
    # print(words["head"])
    # print(len(words["head"]))

    # create write data
    for word in search:
        writeStuff += word + "," + str(len(words.get(word))) + "\n"

    # write to file        
    try:
        with open(out, "w") as write:
            write.write(writeStuff)
    except:
        print("error writing file")

def main():
    try:
        with open("dictall.txt", "rU") as temp:
            data = set()
            # create set of all 4 letter words to pass on
            data = {word for word in temp.read().split("\n") if len(word) == 4}
    except:
        print("error while opening file.")

    # do(sys.argv[1], sys.argv[2], data)
    do("inp.txt", "out.txt", data)
    # do(data)

main()