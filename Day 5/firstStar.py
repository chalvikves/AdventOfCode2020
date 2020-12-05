def read_input():
    with open(file = 'input.txt', mode = 'r') as f:
        return f.read().split("\n")
        
def read_test_input():
    with open(file = 'test.txt', mode = 'r') as f:
        return f.read().split("\n")
          
inp = read_input()

def findRow(letter, high, low):
    mid = low + (high - low) // 2
    if high == low:
        return [low, high]
    if letter in "F" or letter in 'L':
        return [low, mid]
    else:
        return [mid+1, high]

highest = []

for i in inp:
    temp = list(range(0, 128))
    tema = list(range(0, 8))

    for n in i:
        if n == 'R' or n == 'L':
            tema = findRow(n, max(tema), min(tema))
        if n == 'F' or n == 'B':
            temp = findRow(n, max(temp), min(temp))
        
    row = temp[0]
    column = tema[0]
    seatID = row * 8 + column
    highest.append(seatID)
    #print(f'row: {row}, column: {column}, seat ID: {seatID}')

print(max(highest))
