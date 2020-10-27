if __name__ == '__main__':
    n = int(input())
    a =[]
    for i in range(1,n+1):
        a.append(str(i))
    
    new = ''
    for j in a:
        new+=j

    print(new)
