import numpy as np;

# part 1
def parseInput():
    numbers = []
    boards = []

    board = np.empty((5,5), dtype=object)
    r = 0

    for pos, line in enumerate(open('input')):
        line = line.strip()
        if pos == 0:
            numbers = [x for x in line.split(',')]
            continue
        if r == 5:
            boards.append(board)
            board = np.empty((5,5), dtype=object)
            r = 0
        if not line:
            continue
        board[r] = [x for x in line.split(' ') if x]
        r += 1
    boards.append(board)
    return boards, numbers

def search1(boards, numbers):
    for num in numbers:
        for board in boards:
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if board[r][c] == num:
                        board[r][c] = board[r][c] + '*'
                        if all('*' in x for x in board[r,:]) or all('*' in x for x in board[:,c]):
                            return board, int(num)

boards1, numbers1 = parseInput()
w1, n1 = search1(boards1, numbers1)
s1 = 0
for r in range(len(w1)):
    for c in range(len(w1[r])):
        if '*' not in w1[r,c]:
            s1 += int(w1[r,c])
print(s1 * n1)

# part 2
def search2(boards, numbers):
    winners = set()
    winners_max = len(boards)
    for num in numbers:
        for bidx, board in enumerate(boards):
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if board[r][c] == num:
                        board[r][c] = board[r][c] + '*'
                        if all('*' in x for x in board[r,:]) or all('*' in x for x in board[:,c]):
                            winners.add(bidx)
                            if (len(winners) == winners_max):
                                return board, int(num);

boards2, numbers2 = parseInput()
w2, n2 = search2(boards2, numbers2)
s2 = 0
for r in range(len(w2)):
    for c in range(len(w2[r])):
        if '*' not in w2[r,c]:
            s2 += int(w2[r,c])
print(s2 * n2)