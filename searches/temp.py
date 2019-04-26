# try:
#     with open(sys.argv[1], "rU") as temp:
#         length = len(temp.read().split("\n")[0].split(",")[0])
# except:
#     print("error finding length of input words")
try:
    with open("dictall.txt", "rU") as temp:
        data = set()
        # create set of all 4 letter words to pass on
        data = {word for word in temp.read().strip().split("\n") if len(word) <= 6}
except:
    print("error while opening file.")

print(data, len(data))
