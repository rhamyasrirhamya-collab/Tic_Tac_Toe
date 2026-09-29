# TIC-TAC-TOE USING MINIMAX

b = [' '] * 9

def show():
    print(b[0], '|', b[1], '|', b[2])
    print('--+---+--')
    print(b[3], '|', b[4], '|', b[5])
    print('--+---+--')
    print(b[6], '|', b[7], '|', b[8])

def win(p):
    return any(b[a] == b[c] == b[d] == p for a,c,d in
               [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
                (1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def minimax():
    if win('O'): return 1
    if win('X'): return -1
    if ' ' not in b: return 0

    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            scores.append(-minimax())
            b[i] = ' '
    return max(scores)

print("TIC-TAC-TOE")
print("You = X   AI = O")

while True:
    show()
    n = int(input("Enter position (1-9): ")) - 1
    b[n] = 'X'

    if win('X'):
        show(); print("You win!"); break

    if ' ' not in b:
        show(); print("Draw!"); break

    best, move = -2, 0
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            s = -minimax()
            b[i] = ' '
            if s > best:
                best, move = s, i

    b[move] = 'O'

    if win('O'):
        show(); print("AI wins!"); break

