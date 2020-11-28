def average(array):
    # your code goes here
    new = set(arr)
    return (sum(new)/len(new))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
