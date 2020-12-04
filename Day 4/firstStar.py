def read_input():
    with open(file = 'input.txt', mode = 'r') as f:
        return f.read().split("\n")
        
def read_test_input():
    with open(file = 'test.txt', mode = 'r') as f:
        return f.read().split("\n")
        
        
        
inp = read_input()

dic = {
}
count = 0
sg = []
validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def checkValidity(dic):
    valid = 0
    
    if len(dic) == 8:
        for i in validFields:
            if i in dic:
                valid += 1
        
    
    elif len(dic) == 7:
        for i in validFields:
            if i == 'cid':
                if i not in dic:
                    valid += 1 
            else:
                valid += 1

    return valid == 8

for j in inp:
    tem = j.split(' ')
    for i in tem:
        sg.append(i.replace("\n", " "))



for i in sg:
    
    if i != '':
        
        temp = i.split(':')
        dic[temp[0]] = temp[1]
         
    else:
        if checkValidity(dic):
            count += 1
        dic = {}
       
print(count)