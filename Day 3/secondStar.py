def read_input():
    with open(file = 'input.txt', mode = 'r') as f:
        return f.read().split("\n")
        
        
inp = read_input()


def traverse(right, down):
    trees = 0
    ip = down
    ind = right
    
    while ip < len(inp):
        
        if ind >= len(inp[0]): 
            ind = ind - 31
        
        if inp[ip][ind] == "#":
            trees += 1

        ind += right
        ip += down
        
    return trees

print(traverse(1,1) * traverse(3, 1) * traverse(5,1) * traverse(7,1) * traverse(1,2))