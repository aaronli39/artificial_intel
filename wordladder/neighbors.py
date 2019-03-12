import sys

def main():
    try:
        with open("dictall.txt", "rU") as temp:
            dat = temp.read().split("\n")
            data = [i for i in dat if len(i) == 4]
        # print(data, len(data))
    except:
        print("error while opening file.")

main()