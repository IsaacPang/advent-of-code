# read in data
# remove the newline character in the txt file
with open('data.txt', 'r') as f:
    l = [i.rstrip('\n') for i in f.readlines()]

# Problem 1
# get the start and end of the rule range
# get the letter and password for each row
from collections import Counter

def between(x, y, n):
    return (x <= n <= y)

valid = 0
for row in l:
    rule, password = row.split(': ')
    ranges, letter = rule.split(' ')
    start, end = list(map(int, ranges.split('-')))
    d = Counter(password)
    valid += between(start, end, d[letter])

print(f'Valid passwords (Problem 1): {valid}')

# Problem 2
valid = 0
for row in l:
    rule, pw = row.split(': ')
    ranges, a = rule.split(' ')
    s, e = list(map(lambda x: int(x) - 1, ranges.split('-')))
    condition = (pw[s] == a or pw[e] == a) and not (pw[s] == a and pw[e] == a)
    valid += condition

print(f'Valid passwords (Problem 2): {valid}')