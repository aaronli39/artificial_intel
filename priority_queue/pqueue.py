#! /usr/bin/python3

import sys

# default comparison
def ord_cmp(a, b):
    if a < b:
        return -1
    if a == b:
        return 0
    return 1

# priority queue
class Pqueue:
    # init initializes the array, size, and comparator obj
    def __init__(self, comparator=ord_cmp):
        self.data = []
        self.size = 0
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

        while(self.cmp_to(self.data[el], self.data[par]) == -1 and par >= 0):
            self.data[el], self.data[par] = self.data[par], self.data[el]
            # set new vals to bubble up
            el = par
            par = int((par - 1) / 2)
        # print(self.data, val)

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
        if self.size == 2 and self.cmp_to(self.data[cur], self.data[left]) == 1:
            self.data[cur], self.data[left] = self.data[left], self.data[cur]

        while(left < self.size and right < self.size and
              (self.cmp_to(self.data[cur], self.data[left]) == 1 or self.cmp_to(self.data[cur], self.data[right]) == 1)):
            # if left smaller than right
            if self.cmp_to(self.data[left], self.data[right]) == 1:
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
        return self.data[0]

    # returns list representation of the queue
    def toList(self):
        ret = [self.pop() for i in self.data]
        return ret
    
    # returns the elements in the queue without popping
    def internal_list(self):
        return self.data

# Testing
a = Pqueue()
a.push_all(list('PETERBR'[::-1]))
print(a.internal_list())
a.pop()
a.pop()
print(a.internal_list())
# print("toList():", a.toList())
# a.pop()
# print('boi: {}'.format(str(a.data)))
