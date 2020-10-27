if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxm = max(arr)
    temp = -101
    for i in range(len(arr)):
        if(arr[i]<maxm and arr[i]>temp):
            temp = arr[i]
        
    print(temp)
