# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())

rooms = list(map(int, input().split()))

count = {}

for room in rooms:
    if room in count:
        count[room] += 1
    else:
        count[room] = 1
        
for i in count:
    if count[i] != k:
        print(i)