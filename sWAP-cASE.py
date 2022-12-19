def swap_case(s):
    ans = list(s)
    ansStr = ""
    for i in range(len(ans)):
        if ans[i].isalpha():
            if ans[i].islower():
                ans[i] = ans[i].upper()
            else:
                ans[i] = ans[i].lower()
            
    for i in range(len(ans)):
        ansStr += ans[i]
    return ansStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)