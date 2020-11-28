# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = list(map(int, input().split()))
n = int(input())
b = list(map(int, input().split()))
a = set(a)
b = set(b)
u = a.union(b)
i = a.intersection(b)
res = sorted(u.difference(i))
for i in range(len(res)):
    print(res[i])
