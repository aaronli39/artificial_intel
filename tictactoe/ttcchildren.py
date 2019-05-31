""" Layout positions:
0 1 2
3 4 5
6 7 8
"""
# layouts look like "_x_ox__o_"

Wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

# this is a dictionary with key = a layout, and value = its corresponding BoardNode
AllBoards = ({})

startBoard = "_________"


# the class
class BoardNode:
    def __init__(self, layout):
        self.layout = layout
        self.endState = (
            None
        )  # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = []  # all layouts that can lead to this one, by one move
        self.children = [
        ]  # all layouts that can be reached with a single move

    def print_me(self):
        print("layout:", self.layout, "endState:", self.endState)
        print("parents:", self.parents)
        print("children:", self.children)


# what an endstate is
def endState(board):
    for winCond in Wins:
        if (board[winCond[0]] == board[winCond[1]]
                and board[winCond[1]] == board[winCond[2]]
                and board[winCond[0]] != "_"):
            if board[winCond[0]] == "x":
                return (True, "x")
            return (True, "o")
    if board.count("_") == 0:
        return (False, "d")
    return (False, None)


# recursive solution
def CreateAllBoards(layout, parent):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    global AllBoards

    node = BoardNode(layout)
    if parent != None:
        node.parents += [parent]
    node.endState = endState(layout)[1]
    AllBoards[layout] = node

    if node.endState == "x" or node.endState == "o" or node.endState == "d":
        return

    move = "_"
    if layout.count("x") == layout.count("o"):
        move = "x"
    else:
        move = "o"

    for i in range(9):
        if layout[i] == "_":
            newLayout = layout[:i] + move + layout[i + 1:]
            node.children += [newLayout]
            CreateAllBoards(newLayout, layout)


# number of children in allboards
def numChildren(all):
    childrenSum = 0
    for i in all.keys():
        childrenSum += len(all[i].children)
    return childrenSum


# create all the end state statistics
def countEndState(all):
    x_wins, o_wins, draws, not_ends = 0, 0, 0, 0
    for i in all.keys():
        if all[i].endState == "x":
            x_wins += 1
        if all[i].endState == "o":
            o_wins += 1
        if all[i].endState == "d":
            draws += 1
        if all[i].endState == None:
            not_ends += 1
    return (str(x_wins), str(o_wins), str(draws), str(not_ends))


CreateAllBoards(startBoard, None)

# store the board nums
numBoards = len(AllBoards)
numChildren = numChildren(AllBoards)
endStates = countEndState(AllBoards)

print("Number of Boards: " + str(numBoards))  # 5478
print("Number of Children: " + str(numChildren))  # 16167
print("Number of x_winning: " + endStates[0])  # 626
print("Number of o_winning: " + endStates[1])  # 316
print("Number of draws: " + endStates[2])  # 16
print("Number of not_ends: " + endStates[3])  # 4520
