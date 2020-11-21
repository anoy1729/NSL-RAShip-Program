import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = []
for i in range(n):
    l.append(list(map(str, input().strip().split(' ')))) 
    
for i in range(n): 
    pattern = r"^[+|-]?[0-9]*[.]+[\d]*$"
    if re.match(pattern, l[i][0]):
        print(True)
    else:
        print(False)
