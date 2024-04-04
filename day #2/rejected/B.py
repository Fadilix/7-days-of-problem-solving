C, n = map(int, input().split())

arr = []
while n:
    arr.append(list(map(int, input().split())))
    n -= 1

# number of people do not exceed the capacity (c) or be below 0
# no passenger waited when train[0] < people waiting
# print(arr)

# def peopleInTheTrain(): # do not consider this function
#     count = 0
#     for train in arr:
#         count += (train[1] - train[0])


def solve():
    # check for the last waiting
    if arr[-1][-1] > 0:
            return False
    
    people = 0
    for i, train in enumerate(arr):
        people -= train[0]
        people += train[1]
        waiting = train[2]

        # print("People:", people)
        
        # check if there is still people in the last train
        if i == len(arr) - 1:
            if people > 0:
                return False

        # is there room for the people waiting ?
        # print("Room:", C - people)
        # print("Waiting...", waiting)
      
        if (people > C) or (C - people > waiting + 1) or (people < 0):
            return False
        
    return True

print("possible" if solve() else "impossible")