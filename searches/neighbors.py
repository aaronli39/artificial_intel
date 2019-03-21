#! /usr/bin/python3

import sys

def comp(a, b, end):
        ac, bc = 0, 0
        # print(a, b)
        for i in range(4): 
            if a[1][i] == end[i]: ac += 1
        for i in range(4): 
            if b[1][i] == end[i]: bc += 1
        if (ac + a[0]) < (bc + b[0]): return 1
        elif (ac + a[0]) == (bc + b[0]): return 0
        return -1

# priority queue
class Pqueue:
    # default comparison
    # a and b are lists [steps, word]
    def ord_cmp(self, a, b, end):
        ac, bc = 0, 0
        # print(a, b)
        for i in range(self.len): 
            if a[1][i] == end[i]: ac += 1
        for i in range(self.len): 
            if b[1][i] == end[i]: bc += 1
        # print(a, b, ac - a[0], bc - b[0])
        if (ac - a[0]) < (bc - b[0]): return 1
        elif (ac - a[0]) == (bc - b[0]): return 0
            # if a[0] < b[0]: return -1
            # return 1
        return -1

    # init initializes the array, size, and comparator obj
    def __init__(self, length, result, comparator=ord_cmp):
        self.data = []
        self.size = 0
        self.len = length
        self.end = result
        self.cmp_to = comparator

    # push takes in 1 val, appends it, and bubbles the
    # val to appropriate position
    def push(self, val):
        # add element
        self.data.append(val)
        self.size += 1
        # bubble up
        el = self.size - 1
        par = int((self.size - 2) / 2)

        while(self.cmp_to(self, self.data[el], self.data[par], self.end) == -1 and par >= 0):
            self.data[el], self.data[par] = self.data[par], self.data[el]
            # set new vals to bubble up
            el = par
            par = int((par - 1) / 2)

    # pushL takes in a list, appends each value in list to 
    # queue, and the bubbles them to their correct location 
    def push_all(self, data):
        [self.push(i) for i in data]
        return

    # pop root, rearrange rest of array
    def pop(self):
        # return none if nothing
        if self.size == 0: return None
        # set return value
        ret = self.data[0]
        # set new root as last element to bubble down
        self.data[0] = self.data[self.size - 1]
        self.data, self.size = self.data[:-1], self.size - 1

        # starting indices with left and right children
        cur = 0
        left, right = 2 * cur + 1, 2 * cur + 2

        # if it's just a one level tree, pop root and swap left and current if necessary
        if self.size == 2 and self.cmp_to(self, self.data[cur], self.data[left], self.end) == 1:
            self.data[cur], self.data[left] = self.data[left], self.data[cur]

        while(left < self.size and right < self.size and
              (self.cmp_to(self, self.data[cur], self.data[left], self.end) == 1 or self.cmp_to(self, self.data[cur], self.data[right], self.end) == 1)):
            # if left smaller than right
            if self.cmp_to(self, self.data[left], self.data[right], self.end) == 1:
                # right smaller so swap right and current
                self.data[cur], self.data[right] = self.data[right], self.data[cur]
                cur = right
                left, right = cur * 2 + 1, cur * 2 + 2
            else:
                # swap left and current
                self.data[cur], self.data[left] = self.data[left], self.data[cur]
                cur = left
                left, right = cur * 2 + 1, cur * 2 + 2
        return ret

    # look at next root
    def peek(self):
        if self.size == 0: return None
        return self.data[0][1]

    # returns list representation of the queue
    def toList(self):
        ret = [self.pop() for i in self.data]
        return ret
    
    # returns the elements in the queue without popping
    def internal_list(self):
        return self.data

def ladder(words, length, start, end):
    ret, steps, explored = [start], 1, set()
    # start word ladder
    if words.get(start):
        queue = Pqueue(length, end)
        for i in words.get(start):
            queue.push([1, i])
            explored.add(i)
        if queue.peek() == end:
            return [start, end]


        frontier, explored, path, currNeighbors = [], set(), [], [start]
        dict = (masterDict(len(start)))
        while True:
            # push neighbors onto frontier
            for neighbor in currNeighbors:
                push(frontier, (getCost(neighbor, target) + len(path), neighbor, path) )
            # no neighbors means no word ladder for the start -> target
            if len(frontier) == 0:
                return [start, target]
            shortest = pop(frontier)
            print(shortest[1], shortest[2], shortest[2] + [shortest[1]])
            if shortest[1] == target:
                return shortest[2] + [shortest[1]]
            else:
                if shortest[1] not in explored:
                    # add to explored words
                    explored.add(shortest[1])
                    path = shortest[2] + [shortest[1]]
                    currNeighbors = [word for word in dict[shortest[1]] if word not in explored]
                else:
                    path = []
                    currNeighbors = []


        while queue.peek():
            if queue.peek() == end:
                ret.append(queue.pop())
                return ret
            elif 

def do(inp, out, data, length):
    # vars to use
    alpha = "abcdefghijklmnopqrstuvwxyz"
    words = {}
    writeStuff = ""
    search = []
    try:
        with open(inp, "rU") as inFile:
            search = inFile.read().split("\n")
            start = search[0]
            end = search[1]
    except:
        print("error reading input file")
        return

    # create the dictionary of words of desired length
    for i in data:
        ind = 0
        neighbors = set()
        while ind < length:
            for letter in alpha:
                word = i[:ind] + letter + i[ind + 1:]
                if word in data and word != i:
                    neighbors.add(word)
            ind += 1

        words[i] = list(neighbors)
    
    result = ladder(words, length, start, end)

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
        with open(sys.argv[1], "rU") as temp:
            length = len(temp.read().split("\n")[0].split(",")[0])
    except:
        print("error finding length of input words")
    try:
        with open("dictall.txt", "rU") as temp:
            data = set()
            # create set of all 4 letter words to pass on
            data = {word for word in temp.read().strip().split("\n") if len(word) == length}
    except:
        print("error while opening file.")
    do(sys.argv[1], sys.argv[2], data, length)
    # do("inp.txt", "out.txt", data)
    # do(data)

main()
# a = Pqueue(4, "dead")
# a.push([1, "heal"])
# a.push([1, "heat"])
# a.push([1, "dead"])
# a.push([1, "lead"])
# a.push([1, "teal"])
# a.push([2, "bait"])
# a.push
# # print(comp([1, "head"], [1, "teal"], "tail"))
# print(a.internal_list())