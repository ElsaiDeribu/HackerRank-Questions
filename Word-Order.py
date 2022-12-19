# Enter your code here. Read input from STDIN. Print output to STDOUT

count = {}
n = int(input())

for i in range(n):
    word = input()
    
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
 
print(len(count))
for i in count:
    print(count[i], end = " ")
    

