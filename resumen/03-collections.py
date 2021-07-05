from collections import Counter, namedtuple, deque

c = Counter(['a', 'a', 'a', 'b'])
c['a'] # 3
c['c'] # 0
c.most_common() # [('a', 3), ('b', 1)]

Point = namedtuple('Point', 'x y z')
point = Point(3, 4, 5)
point.x   # 3
point[0]  # 3

d = deque([1,2,3], maxlen=3)
d           # 1 2 3
d.append(4) # 2 3 4
d.popleft() # 2