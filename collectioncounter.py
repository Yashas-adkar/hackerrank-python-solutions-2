# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Number of shoes
X = int(input())

# Shoe sizes available
sizes = list(map(int, input().split()))

# Count each size
shoe_count = Counter(sizes)

# Number of customers
N = int(input())

earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    
    if shoe_count[size] > 0:
        earnings += price
        shoe_count[size] -= 1

print(earnings)