# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
t = 1
for i in range(n//2):
    a = '.|.'
    a = a*t
    print(a.center(m,'-'))
    t+=2
print('WELCOME'.center(m,'-'))

for i in range(n//2):
    t-=2
    a = '.|.'
    a = a*t
    print(a.center(m,'-'))
