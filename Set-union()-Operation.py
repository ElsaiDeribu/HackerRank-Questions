# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
english = set(input().split())
_ = input() 
french = set(input().split())

print(len(english | french))
