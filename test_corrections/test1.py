#!/usr/bin/python3

import sys

def prob1(inp, out):
    try:
        f = open(inp, "rU")
        t = f.read().split("\n")
        f.close()
    except:
        print("bad sht occured")
    
    temp, res = [], []
    for i in t:
        temp = i.split(",")
        # first error: i used 0 instead of 2
        # also gotta check for correct indicies
        if len(temp[1:]) >= 2: 
            print(temp)
            name = temp[0]
            # error two: I set temp to
            # .sort().insert() which doesn't
            # return anything
            temp = sorted(temp[1:])
            temp.insert(0, name)
            res.append(",".join(temp))
        else:
            pass
    try:
        # print(res)
        f = open(out, "w")
        # messesd by the order of .join()
        f.write("\n".join(res))
        f.close()
    except:
        print("bad")

def main():
    prob1(sys.argv[1], sys.argv[2])

class Node:  
    # these contain only data, so
    # only __init__() is necessary
    # self.next and self.previous will be used as 
    # pointers in the linked list
    def __init__(self,value):
        self.value = value
        self.next = None       
        self.previous = None

class Dlist:
    def __init__(self):
        # i forgot to have a tail and a size 
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, value):
        val = Node(value)

        if self.head == None:
            self.head, self.tail = val, val
        elif value <= self.head.value:
            self.head.previous = val
            val.next = self.head
            self.head = val
        elif value >= self.tail.value:
            self.tail.next = val
            val.previous = self.tail
            self.tail = val
        else:
            temp = self.head
            while value > temp.value:
                temp = temp.next
            temp.previous.next = val
            val.previous = temp.previous
            temp.previous = val
            val.next = temp
        self.size += 1

    def delete(self, value):
        # print(self.head.value, self.tail.value)
        # print(a)
        if self.head == None or self.head.value < value:
            return False
        elif self.head.value == value:
            if self.tail.value == self.head.value:
                self.head, self.tail = None, None
            else:
                self.head = self.head.next
                self.head.previous = None
            self.size -= 1
            return True
        else:
            def d(self, curr, value):
                if curr.next.value == value:
                    if curr.next.next == None:
                        curr.next = None
                        self.tail = curr
                    else:
                        curr.next = curr.next.next
                        curr.next.next.previous = curr
                    self.size -= 1
                    return True
                elif curr.next == self.tail and value != self.tail.value:
                    return False
                else:
                    return self.d(curr.next, value)
            return d(self, self.head, value)

    def tolist(self):
        ret = []
        while self.head:
            ret.append(self.head.value)
            self.delete(self.head.value)
        return ret

def insert_all(the_dlist, the_input_list):
    for element in the_input_list:
        the_dlist.insert(element)

a = Dlist()
insert_all(a,[4,5,2,3,2,7])
print(a.tolist())
