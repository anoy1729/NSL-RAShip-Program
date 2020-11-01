if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        arr = list(map(str, input().strip().split(' ')))
        if(len(arr)==2):
            arr[1] = int(arr[1])
        elif(len(arr)==3):
            arr[1] = int(arr[1])
            arr[2] = int(arr[2])
        
        if(arr[0]=='insert'):
            lst.insert(arr[1],arr[2])
        if(arr[0]=='print'):
            print(lst)
        if(arr[0]=='remove'):
            lst.remove(arr[1])
        if(arr[0]=='append'):
            lst.append(arr[1])
        if(arr[0]=='sort'):
            lst.sort()
        if(arr[0]=='pop'):
            lst.pop()
        if(arr[0]=='reverse'):
            lst.reverse()
