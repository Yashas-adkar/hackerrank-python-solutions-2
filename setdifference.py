n=int(input())
e=set(map(int,input().split()))
b=int(input())
f=set(map(int,input().split()))
only_english=e-f
print(len(only_english))