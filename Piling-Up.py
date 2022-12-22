# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for i in range(t):
    pile = []
    n = int(input())
    blocks = list(map(int, input().split()))
    l = 0
    r = n - 1
    flag = True
    while l < r:
        if blocks[l] <= blocks[r]:
            if pile and pile[-1] < blocks[r]:
                flag = False
                print("No")
                break
            pile.append(blocks[r])
            r -= 1
            
        else:
            if pile and pile[-1] < blocks[l]:
                flag = False
                print("No")
                break
            pile.append(blocks[l])
            l += 1
    if flag:        
        print("Yes")