def solve():
    possible = True
    cap, n = map(int, input().split())
    passengers = 0
    while n:
        n -= 1
        left, entered, waiting = map(int, input().split())
        if not (0 <= left <= passengers):
            possible = False
        passengers -= left
        if not (0 <= entered <= cap - passengers):
            possible = False
        passengers += entered
        if 0 > waiting or (cap > passengers and waiting > 0):
            possible = False

    print("possible" if possible and passengers == 0 else "impossible")


solve()
