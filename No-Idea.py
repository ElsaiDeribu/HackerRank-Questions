# Enter your code here. Read input from STDIN. Print output to STDOUT

happiness = 0

temp = map(int, input().split())
n = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in range(len(n)):
    if n[i] in A:
        happiness += 1
    elif n[i] in B:
        happiness -= 1
        
print(happiness)