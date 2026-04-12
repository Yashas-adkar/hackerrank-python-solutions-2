n=int(input())
for _ in range(n):
    number=input()
    if (len(number)==10 and number.isdigit() and number[0] in ['7','8','9']):
        print("YES")
    else:
        print("NO")