

def read_input():
    with open(file = 'input.txt', mode = 'r') as f:
        return f.read().split("\n")
        
inp = read_input()

count = 0

for i in inp:
    ind = i.find(":")
    
    rang = i[0:ind-2].split("-")
    
    letter = i[ind-1:ind]
    password = i[ind+2:]

    if password.count(letter) in range(int(rang[0]), int(rang[1])+1):
        count += 1

print(count)
        
