import textwrap

def wrap(string, max_width):
    ans = ''
    count = 0
    for i in string:
        if count == max_width:
            ans += '\n'
            count = 0
        ans += i
        count += 1
    
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)