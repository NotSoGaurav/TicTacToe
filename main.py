import sys

b = [" "] * 9

def pr():
    print()
    print(b[0] + " | " + b[1] + " | " + b[2])
    print("--+---+--")
    print(b[3] + " | " + b[4] + " | " + b[5])
    print("--+---+--")
    print(b[6] + " | " + b[7] + " | " + b[8])
    print()

def em(board):
    return [i for i, v in enumerate(board) if v == " "]

def wn(board):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,c,d in w:
        if board[a] == board[c] == board[d] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "d"
    return None

def mm(board, pl, ai, hu, d=0):
    r = wn(board)
    if r == ai:
        return {"s": 10 - d}
    if r == hu:
        return {"s": d - 10}
    if r == "d":
        return {"s": 0}
    moves = []
    for i in em(board):
        board[i] = pl
        nxt = hu if pl == ai else ai
        res = mm(board, nxt, ai, hu, d+1)
        moves.append({"i": i, "s": res["s"]})
        board[i] = " "
    if pl == ai:
        best = moves[0]
        for m in moves:
            if m["s"] > best["s"]:
                best = m
    else:
        best = moves[0]
        for m in moves:
            if m["s"] < best["s"]:
                best = m
    return best

def am(ai, hu):
    e = em(b)
    if not e:
        return
    if len(e) == 9:
        b[4] = ai
        print("AI 5")
        return
    m = mm(b, ai, ai, hu)
    b[m["i"]] = ai
    print("AI", m["i"]+1)

def hm():
    while True:
        x = input("Pos 1-9 (q quit): ").strip()
        if x.lower() == "q":
            return None
        if x.isdigit():
            p = int(x)-1
            if 0 <= p <= 8:
                if b[p] == " ":
                    return p
        print("bad")

print("TicTacToe MinMax")
print("You:X AI:O")
print()
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")
print()

x = "X"
o = "O"
t = "X"

try:
    while True:
        pr()
        if t == x:
            mv = hm()
            if mv is None:
                print("bye")
                break
            b[mv] = x
        else:
            am(o, x)
        r = wn(b)
        if r:
            pr()
            if r == "d":
                print("Draw")
            elif r == x:
                print("You win")
            else:
                print("AI wins")
            break
        t = o if t == x else x
except KeyboardInterrupt:
    print("\nexited")
    sys.exit(0)