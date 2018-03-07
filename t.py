from collections import defaultdict

lst = ['a', 'b', 'a', 'c', 'b', 'c', 'b', 'a', 'b', 'b', 'c']

count = dict()
for v in lst:
    if v not in count:
        count[v] = 1
    else:
        count[v] += 1

count = defaultdict(int)
for v in lst:
    count[v] += 1
