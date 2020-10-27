if __name__ == '__main__':
    nam = []
    scr = []
    op = []
    for _ in range(int(input())):
        name = input()
        nam.append(name)
        score = float(input())
        scr.append(score)
    minm = min(scr)
    temp = 1000

    for i in range(len(scr)):
        if(scr[i]>minm and scr[i]<temp):
            temp = scr[i]
    
    
    for j in range(len(scr)):
        if scr[j] == temp:
            op.append(nam[j])
    
    op = sorted(op)
    for k in range(len(op)):
        print(op[k])
