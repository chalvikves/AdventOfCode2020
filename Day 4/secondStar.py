import re

def read_input():
    with open(file = 'input.txt', mode = 'r') as f:
        return f.read().split("\n")
        
def read_test_input():
    with open(file = 'test.txt', mode = 'r') as f:
        return f.read().split("\n")
         
inp = read_input()

dic = {}
count = 0
sg = []
validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def checkValid(i, dic):

    if dic.get(i) == None: 
        return False
        
    if i == 'byr' and ( int(dic.get(i)) in range(1920, 2003) ):
        return True 

    if i == 'iyr' and ( int(dic.get(i)) in range(2010, 2021) ):
        return True

    if i == 'eyr' and ( int(dic.get(i)) in range(2020, 2031) ):
        return True

    if i == 'hgt':
        
        if dic.get(i)[-2:] == "in": 
            if int(dic.get(i)[:2]) in range(59, 77):
                return True

        if dic.get(i)[-2:] == "cm":
            if int(dic.get(i)[:-2]) in range(150, 194):
                return True

    if i == 'hcl':
        
        if dic.get(i)[:1] == '#':
            if bool(re.search(r'^[0-9a-f]+$', dic.get(i)[1:])):
                return True

    if i == 'ecl' and dic.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True

    if i == 'pid':
        if len(dic.get(i)) == 9:
            return True

    return False

def checkValidity(dic):
    valid = 0
    
    for i in validFields:
        if i == 'cid':
            valid += 1
        if checkValid(i, dic):
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



     