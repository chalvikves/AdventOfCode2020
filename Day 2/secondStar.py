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
    
    
    if (password[int(rang[0])-1] != letter and password[int(rang[1])-1] != letter) or (password[int(rang[0])-1] == letter and password[int(rang[1])-1] == letter):
        count += 1

        
        

print(1000-count)
        
