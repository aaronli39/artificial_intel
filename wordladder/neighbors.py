import sys

def do(inp, out, data):
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    words = {}
    # print(len(words))
    for i in data:
        ind = 0
        neighbors = []
        while ind < 4:
            for letter in alpha:
                word = i[:ind] + letter + i[ind + 1:]
                if word in data:
                    neighbors.append(word)
            ind += 1
        if i in neighbors:
            neighbors.remove(i)

        words[i] = neighbors
    
    writeStuff = ""
    try:
        with open(inp, "rU") as inFile:
            search = inFile.read().split("\n")
            for word in search:
                writeStuff += word + "," + str(len(words.get(word))) + "\n"
    except:
        print("error reading input file")
    
    try:
        with open(out, "w") as write:
            write.write(writeStuff)
    except:
        print("error writing file")

def main():
    try:
        with open("dictall.txt", "rU") as temp:
            data = set()
            data = {word for word in temp.read().split("\n") if len(word) == 4}
        # print(len(data))
        # print(data)
    except:
        print("error while opening file.")

    # do(sys.argv[1], sys.argv[2], data)
    do("inp.txt", "out.txt", data)
    # do(data)

main()