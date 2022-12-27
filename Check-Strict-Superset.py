# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(input().split())
n = int(input())
ans = True
for i in range(n):
    temp = set(input().split()) 
    if a.intersection(temp) != temp:
        ans = False

        
print(ans)
