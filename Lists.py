if __name__ == '__main__':
    N = int(input())
    ans = []
    
    for i in range(N):
        temp = input().split()
        
        if len(temp) == 3:
            command, arg1, arg2 = temp
            eval("ans." + command + "(" + arg1 + ", " + arg2 + ")" )
            
        elif len(temp) == 2:
            command, arg = temp
            eval("ans." + command + "(" + arg +")")
            
        else:
            if temp[0] == 'print':
                print(ans)
            else:
                eval("ans." + temp[0] + "(" + ")")
            
      