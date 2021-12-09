# read in data
# remove the newline character in the txt file
with open('data', 'r') as f:
    l = [i.rstrip('\n') for i in f.readlines()]
    
with open('test', 'r') as f:
    test = [i.rstrip('\n') for i in f.readlines()]
    
# Problem 1
x = 0
y = 0
path = ''
while y < len(l):
    path += l[y][x % len(l[0])]
    x += 3
    y += 1

from collections import Counter
print(Counter(path))

# Problem 2
rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

from collections import Counter

def get_path(rule, trees):
    x = 0
    y = 0
    path = ''
    while y < len(trees):
        path += trees[y][x % len(trees[0])]
        x += rule[0]
        y += rule[1]

    pathway = Counter(path)
    print(f"Trees encountered, # on slope {rule}: {pathway['#']}")
    return pathway['#']

# Testing
product = 1
for rule in rules:
    product *= get_path(rule, test)
print(f'Final product = {product}')

# Actual problem
product = 1
for rule in rules:
    product *= get_path(rule, l)
print(f'Final product = {product}')