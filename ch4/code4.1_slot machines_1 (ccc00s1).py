chips = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0
machine = 0

while chips >= 1:
    chips = chips - 1

    if machine == 0:
        first = first + 1
        if first == 35:
            first = 0
            chips = chips + 30
    elif machine == 1:
        second = second + 1
        if second == 100:
            second = 0
            chips = chips + 60
    elif machine == 2:
        third = third + 1
        if third == 10:
            third = 0
            chips = chips + 9

    plays = plays + 1
    machine = machine + 1
    if machine == 3:
        machine = 0
        
print('Martha plays', plays, 'times before going broke.')
