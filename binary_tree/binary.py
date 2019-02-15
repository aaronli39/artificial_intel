#! /usr/bin/python3
import sys

class Node:
    def __init__(self, data):
        self.value = data
        self.smaller = None
        self.equal_or_larger = None

    def __str__(self):
        return str(self.value)


class BinTree:
    def __init__(self, A=None):
        # A is an optional argument containing a list of values to be inserted into the binary tree just after cosntruction
        self.root = None
        self.num = 0

    def insert(self, V):
        # inserts a new value
        if self.has(V):
            return
        if self.root == None:
            self.root = Node(V)
        else:
            self.insertt(self.root, V)

    def insertt(self, node, V):
        if V < node.value:
            #           print("smaller than " + str(self.root))
            if node.smaller == None:
                node.smaller = Node(V)
            else:
                self.insertt(node.smaller, V)
        else:
            #           print("larger than " + str(self.root))
            if node.equal_or_larger == None:
                node.equal_or_larger = Node(V)
            else:
                self.insertt(node.equal_or_larger, V)

    def has(self, V):
        # returns True if V is in the list, else False
        if self.root == None:
            return False
        else:
            return self.hass(self.root, V)

    def hass(self, root, V):
        #         print("\n")
        #         print(root.value, V)
        if root.value == V:
            #           print("asdfasdf")
            return True
        elif V < root.value and root.smaller != None:
            #           print("smaller")
            return self.hass(root.smaller, V)
        elif V > root.value and root.equal_or_larger != None:
            #           print("larger")
            return self.hass(root.equal_or_larger, V)
        else:
            #           print("ha")
            return False

    def get_ordered_list(self):
        # returns a list of all values in ordered sequence
        if not self.root:
            return []
        ret = []
        self.adding(self.root, ret)
        return ret

    def adding(self, node, ret):
        if node.smaller:
            self.adding(node.smaller, ret)
        ret.append(node.value)
        if node.equal_or_larger:
            self.adding(node.equal_or_larger, ret)

    def clear(self):
        # clears the list of all nodes
        #         self.root = None
        self.size = 0
        if self.root:
            self.clearr(self.root)
            self.root = None
        else:
            return None

    def clearr(self, node):
        if node.smaller:
            self.clearr(node.smaller)
        node.smaller == None
        if node.equal_or_larger:
            self.clearr(node.equal_or_larger)
        node.equal_or_larger == None

    def has_depth(self, V):
        if self.root == None:
            return None
        else:
            if self.root.value == V:
                return 1
            return 1 + self.depth(self.root, V)

    def depth(self, node, val):
        if node.value == val:
            return 0
        if node.smaller and val < node.value:
            return 1 + self.depth(node.smaller, val)
        elif node.smaller == None and val < node.value:
            return 0
        if node.equal_or_larger and val > node.value:
            return 1 + self.depth(node.equal_or_larger, val)
        elif node.equal_or_larger == None and val > node.value:
            return 0


def Process(inp, out):
    try:
        f = open(inp, "rU") 
        lines = f.read().split("\n")
        f.close()
    except:
        print("error occured!")
        return

    words = lines[0].split(",")
    ints = [int(x) for x in words]
    words = lines[1].split(",")
    haz = [int(x) for x in words]

    answers = []
    temp = BinTree()
    for i in ints: temp.insert(i)
    for i in haz: answers.append(temp.has_depth(i))
    print(sum(answers) / len(answers))
    f = open(out, "w")
    toWrite = [str(x) for x in answers]
    f.write(",".join(toWrite) + "\n")
    f.close()

def main():
    Process(sys.argv[1], sys.argv[2])

main()

# fred = BinTree()
# fred.insert(10)
# fred.insert(15)
# fred.insert(8)
# fred.insert(9)
# fred.insert(9)
# fred.insert(11)
# fred.insert(13)
# fred.insert(17)
# print(fred.has(10))
# print(fred.has(11))
# print(fred.has(9))
# print(fred.has(8))
# print(fred.has(122))
# print(fred.has(19))
# print(fred.get_ordered_list())
# print("\n\n")
# print(fred.has_depth(8))
# print(fred.has_depth(11))
# print(fred.has_depth(17))
# Process("inp.txt", "out.txt")
# fred.clear()
# print(fred.get_ordered_list())
# print(fred.has(10))
# temp = fred.has(12)
# print(temp)
