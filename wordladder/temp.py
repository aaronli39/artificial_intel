#!/usr/bin/python3

with open("dictall.txt", "rU") as temp:
    data = set()
    # create set of all 4 letter words to pass on
    data = {x.strip() for x in temp if len(x) == 5}

print(len(data))