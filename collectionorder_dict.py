n=int(input())
items={}
for _ in range(n):
    data=input().split()
    prize=int(data[-1])
    name=" ".join(data[:-1])
    if name in items:
        items[name]+=prize
    else:
        items[name]=prize
for name,prize in items.items():
    print(name,prize)