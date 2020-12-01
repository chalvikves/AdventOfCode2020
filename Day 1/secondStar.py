import list as li

def main():
    listEntries = li.listOfEntries

    for i in listEntries:
        for j in listEntries:
            for k in listEntries:
                if i + j + k == 2020:
                    print(str(i) + ' ' + str(j) + ' ' + str(k))
                    return print(i*j*k)
        
main()
