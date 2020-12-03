def read_input():
    with open(file = 'input.txt', mode = 'r') as f:
        return f.read().split("\n")
        
        
inp = read_input()


def traverse():
    trees = 0
    ip = 1
    ind = 3
    
    while ip < len(inp):
        
        if ind >= len(inp[0]): 
            ind = ind - 31
        
        if inp[ip][ind] == "#":
            trees += 1

        ind += 3
        ip += 1
        
    return trees

print(traverse())