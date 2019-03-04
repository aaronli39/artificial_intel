# #!/usr/bin/python3

# import sys


# def ord_cmp(a, b):  # ordinary cmp_to fxn
#     if a < b:
#         return -1
#     if a == b:
#         return 0
#     return 1


# class Pqueue:
#     def __init__(self, comparator=ord_cmp):
#         self.data = []
#         self.size = 0
#         self.cmp_to = comparator

#     def push(self, val):
#         # add element
#         self.size += 1
#         self.data.append(val)
#         # bubble up
#         el, par = self.size - 1, int((self.size - 1) / 2)

#         while(self.cmp_to(self.data[el], self.data[par]) == -1):
#             temp = self.data[el]
#             self.data[el] = self.data[par]
#             self.data[par] = temp
#             # set new vals to bubble up
#             el = par
#             par = int((par - 1) / 2)
#         # print(self.data, val)

#     def pop(self):
#         if self.size == 0:
#             return None
#         ret = self.data[0]
#         self.data[0] = self.data[self.size - 1]
#         self.data, self.size = self.data[:-1], self.size - 1

#         # starting indices with left and right children
#         cur = 0
#         left, right = 2 * cur + 1, 2 * cur + 2

#         # if it's just a one level tree, pop root and swap left and current if necessary
#         if self.size == 2 and self.cmp_to(self.data[cur], self.data[left]) == 1:
#             self.data[cur], self.data[left] = self.data[left], self.data[cur]

#         while(left < self.size and right < self.size and (self.cmp_to(self.data[cur], self.data[left]) == 1
#                                                           or self.cmp_to(self.data[cur], self.data[right]) == 1)):
#             # bubbling down:
#             # if left smaller than right
#             # print("data: ", self.data)
#             # print("left: " + str(self.data[left]), left)
#             # print("right: " + str(self.data[right]), right)
#             # print("curr: ", self.data[cur], cur)
#             # print("cmp: " + str(self.cmp_to(self.data[left], self.data[right])))
#             if self.cmp_to(self.data[left], self.data[right] == -1):
#                 # swap left and current
#                 self.data[cur], self.data[left] = self.data[left], self.data[cur]
#                 cur = left
#                 left, right = cur * 2 + 1, cur * 2 + 2
#             else:
#                 # # right smaller so swap right and current
#                 temp = self.data[cur]
#                 self.data[cur] = self.data[right]
#                 self.data[right] = temp
#                 # self.data[cur], self.data[right] = self.data[right], self.data[cur]
#                 cur = right
#                 left, right = cur * 2 + 1, cur * 2 + 2

#         # print("end :", self.data, "\n")
#         return ret

#     def pope(self):  # pops off the top element and returns it; if empty, returns None
#         if self.size == 0:
#             return None

#         oldroot = self.data[0]

#         self.data[0] = self.data[self.size - 1]
#         del self.data[-1]
#         self.size = self.size - 1

#         current = 0
#         leftchild = 2 * current + 1
#         rightchild = 2 * current + 2

#         #print('leftchild: ' + str(leftchild))
#         #print('rightchild: ' + str(rightchild))

#         if self.size == 2 and self.cmp_to(self.data[current], self.data[leftchild]) == 1:
#             self.data[current], self.data[leftchild] = (
#                 self.data[leftchild], self.data[current])

#         while(leftchild < self.size and rightchild < self.size and
#               (self.cmp_to(self.data[current], self.data[leftchild]) == 1 or self.cmp_to(self.data[current], self.data[rightchild]) == 1)):
#             #print('leftchild: ' + str(leftchild))
#             #print('rightchild: ' + str(rightchild))
#             if self.cmp_to(self.data[leftchild], self.data[rightchild]) == -1:
#                 self.data[current], self.data[leftchild] = (
#                     self.data[leftchild], self.data[current])
#                 current = leftchild
#                 leftchild = current * 2 + 1
#                 rightchild = current * 2 + 2
#             else:
#                 self.data[current], self.data[rightchild] = (
#                     self.data[rightchild], self.data[current])
#                 current = rightchild
#                 leftchild = current * 2 + 1
#                 rightchild = current * 2 + 2

#         return oldroot

#     def peek(self):
#         if self.size == 0:
#             return None
#         return self.data[0]

#     def toList(self):
#         print(self.data, self.size)
#         ret = [self.pop() for i in self.data]
#         return ret

#!/usr/bin/python3

class Pqueue:
    def OrdinaryComparison(a,b): #ordinary compare_to fxn
        if a < b: return -1
        if a == b: return 0
        return 1
    
    def __init__(self, comparator = OrdinaryComparison): #initializes priority queue / heap
        self.info = []
        self.size = 0
        self.compare_to = comparator
                
    def __str__(self): #the to-string method
        return str(self.info)

    
    def push(self, value): #pushs value into heap; sorts it so that parent >= child
        self.info.append(value)
        self.size = self.size + 1

        current = self.size - 1
        parent = int((current - 1) / 2)

        while(self.compare_to(self.info[current], self.info[parent]) == -1 and parent >= 0):
            self.info[current], self.info[parent] = (self.info[parent], self.info[current])

            current = parent
            parent = int((parent - 1) / 2)

    def pop(self): #pops off the top element and returns it; if empty, returns None
        if self.size == 0:
            return None
        
        oldroot = self.info[0]

        self.info[0] = self.info[self.size - 1]
        del self.info[-1]
        self.size = self.size - 1

        current = 0
        leftchild = 2 * current + 1
        rightchild = 2 * current + 2

        #print('leftchild: ' + str(leftchild))
        #print('rightchild: ' + str(rightchild))

        if self.size == 2 and self.compare_to(self.info[current], self.info[leftchild]) == 1:
            self.info[current], self.info[leftchild] = (self.info[leftchild], self.info[current])
        
        while(leftchild < self.size and rightchild < self.size and
              (self.compare_to(self.info[current], self.info[leftchild]) == 1 or self.compare_to(self.info[current], self.info[rightchild]) == 1)):
            #print('leftchild: ' + str(leftchild))
            #print('rightchild: ' + str(rightchild))
            if self.compare_to(self.info[leftchild], self.info[rightchild]) == -1:
                self.info[current], self.info[leftchild] = (self.info[leftchild], self.info[current])
                current = leftchild
                leftchild = current * 2 + 1
                rightchild = current * 2 + 2
            else:
                self.info[current], self.info[rightchild] = (self.info[rightchild], self.info[current])
                current = rightchild
                leftchild = current * 2 + 1
                rightchild = current * 2 + 2
                
        return oldroot
                
    def peek(self): #returns but does not pop top element; if empty, returns None
        if self.size > 0:
            return self.info[0]
        return None

    def size(self): #returns size of the current priority queue / heap
        return self.size

    def tolist(self):
        print(self.info)
        returned_list = []
        size = 0
        while size < len(self.info):
            returned_list.append(self.pop())
        return returned_list

#Testing

a = Pqueue()
a.push(10)
a.push(8)
a.push(5)
a.push(15)
a.push(4)
print(a.tolist())
