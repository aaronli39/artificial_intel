import random
''' 
Layout positions:
0 1 2
3 4 5
6 7 8
'''

# Best future states according to the player viewing this board
ST_X = 1  # X wins
ST_O = 2  # O wins
ST_D = 3  # Draw

states = [
    'top-left', 'top-middle', 'top-right', 'middle-left', 'middle',
    'middle-right', 'bottom-left', 'bottom-middle', 'bottom-right'
]

Wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

AllBoards = {
}  # This is primarily for debugging: key = layout, value = BoardNode


class BoardNode:
    def __init__(self, layout):
        self.layout = layout
        self.mover = 'x' if layout.count('x') == layout.count('o') else 'o'

        self.state = self.this_state(
            layout)  # if final board, then ST_X, ST_O or ST_D, else None
        if self.state is None:
            self.best_final_state = None  # best achievable future state: ST_X, ST_O or ST_D
            self.best_move = None  # 0-9 to achieve best state
            self.num_moves_to_final_state = None  # number of moves to best state
        else:
            self.best_final_state = self.state
            self.best_move = -1
            self.num_moves_to_final_state = 0

        self.children = set()

    def print_me(self):
        print('layout:', self.layout)
        print('mover:', self.mover)
        print('state:', self.str_state(self.state))
        print('best_final_state:', self.str_state(self.best_final_state))
        print('best_move:', self.best_move, self.str_move(self.best_move))
        print('num_moves_to_final_state:', self.num_moves_to_final_state)

    def print_layout(self):
        print('%s\n%s\n%s' % (' '.join(self.layout[0:3]), ' '.join(
            self.layout[3:6]), ' '.join(self.layout[6:9])))

    # =================== class methods  =======================
    def str_state(self, state):
        # human description of a state
        return 'None' if state is None else ['x-wins', 'o-wins', 'draw'
                                             ][state - 1]

    def str_move(self, move):
        # human description of a move
        moves = ('top-left','top-center','top-right',\
                 'middle-left','middle-center','middle-right',\
                 'bottom-left','bottom-center','bottom-right')
        return 'done' if move == -1 else moves[move]

    def this_state(self, layout):
        # classifies this layout as None if not final, otherwise ST_X or ST_O or ST_D
        for awin in Wins:
            if layout[awin[0]] != '_' and layout[awin[0]] == layout[
                    awin[1]] == layout[awin[2]]:
                return ST_X if layout[awin[0]] == 'x' else ST_O
        if layout.count('_') == 0:
            return ST_D
        return None


def CreateAllBoards(layout):
    # Populate AllBoards with finally calculated BoardNodes

    if layout in AllBoards:
        return

    anode = BoardNode(layout)
    # if this is an end board, then all of its properties have already be calculated by __init__()
    if anode.state is not None:
        AllBoards[layout] = anode
        return

    # expand children if this is not a final state
    move = 'x' if layout.count('x') == layout.count('o') else 'o'
    for pos in range(9):
        if layout[pos] == '_':
            new_layout = layout[:pos] + move + layout[pos + 1:]
            if new_layout not in AllBoards:
                CreateAllBoards(new_layout)
            anode.children.add(new_layout)

    # organize children

    bestMoveList = list()
    wins = list()
    draws = list()
    losses = list()
    for child in anode.children:
        if move == "x" and AllBoards[child].best_final_state == ST_X:
            wins += [AllBoards[child]]
        elif move == "o" and AllBoards[child].best_final_state == ST_O:
            wins += [AllBoards[child]]
        elif AllBoards[child].best_final_state == ST_D:
            draws += [AllBoards[child]]
        else:
            losses += [AllBoards[child]]

    # interpret children

    # pick win in lowest moves
    if len(wins) != 0:
        wins.sort(key=lambda x: x.num_moves_to_final_state)
        anode.num_moves_to_final_state = wins[0].num_moves_to_final_state + 1
        if move == "x":
            anode.best_final_state = ST_X
        else:
            anode.best_final_state = ST_O
        bestMoveList = [
            x.layout for x in wins
            if x.num_moves_to_final_state == wins[0].num_moves_to_final_state
        ]
    # pick draw in most moves
    elif len(draws) != 0:
        draws.sort(key=lambda x: x.num_moves_to_final_state, reverse=True)
        anode.num_moves_to_final_state = draws[0].num_moves_to_final_state + 1
        anode.best_final_state = ST_D
        bestMoveList = [
            x.layout for x in draws
            if x.num_moves_to_final_state == draws[0].num_moves_to_final_state
        ]
    # pick loss in most moves
    elif len(losses) != 0:
        losses.sort(key=lambda x: x.num_moves_to_final_state, reverse=True)
        anode.num_moves_to_final_state = losses[0].num_moves_to_final_state + 1
        if move == "o":
            anode.best_final_state = ST_X
        else:
            anode.best_final_state = ST_O
        bestMoveList = [
            x.layout for x in losses
            if x.num_moves_to_final_state == losses[0].num_moves_to_final_state
        ]

    # pick random best move
    if len(anode.children) != 0:
        bestMove = random.choice(bestMoveList)
        for i in range(9):
            if bestMove[i] != anode.layout[i]:
                anode.best_move = i
                break

    AllBoards[layout] = anode


# print everything
def printStuff(layout):
    print("move=" + str(AllBoards[layout].best_move))
    print(states[AllBoards[layout].best_move])
    if AllBoards[layout].best_final_state == 1:
        print("x wins in " + str(AllBoards[layout].num_moves_to_final_state) +
              " moves")
    elif AllBoards[layout].best_final_state == 2:
        print("o wins in " + str(AllBoards[layout].num_moves_to_final_state) +
              " moves")
    else:
        print("draw in " + str(AllBoards[layout].num_moves_to_final_state) +
              " moves")


# test
CreateAllBoards("_________")
printStuff("x_ox_o___")
print("------------------------------------------------")
printStuff("xox_x__o_")
print("------------------------------------------------")
printStuff("xox_x__oo")
print("------------------------------------------------")
printStuff("_________")