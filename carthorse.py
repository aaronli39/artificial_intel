def main():
    l = 9
    for i in "abcdefghijklmnopqrstuvwxyz":
        for x in range(l):
            temp = "carthorse"[:x] + i + "carthorse"[x + 1:]