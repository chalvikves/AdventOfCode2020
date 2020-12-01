import list as li

def main():
    listEntries = li.listOfEntries

    for i in listEntries:
        for j in listEntries:
            if i + j == 2020:
                print(str(i) + ' ' + str(j))
                return print(i*j)
        
main()
