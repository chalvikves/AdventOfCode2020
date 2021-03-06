from entries import listOfEntries

# Time N * log N
def main():
    listEntries = listOfEntries

    def binarySearch (arr, l, r, x): 
        arr.sort()
        if r >= l: 
            mid = l + (r - l) // 2
            
            if arr[mid] == x: 
                return mid 
            
            elif arr[mid] > x: 
                return binarySearch(arr, l, mid-1, x) 
    
            else: 
                return binarySearch(arr, mid + 1, r, x) 
    
        else: 
            return -1

    for i in listEntries:
        rem = 2020 - i
        if binarySearch(listEntries, 0, len(listEntries)-1, rem):
            return print(i*rem)

    
        
main()
