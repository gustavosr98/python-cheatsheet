# HELLO
name = "Gustavo"
print(f"Hello {name} " * 2, " Bye", sep="|" ,end=".\n") # Hello Gustavo Hello Gustavo | Bye.

# LIST
l: list = ["A", "B", "C", "D"] + ["E"]
len(l)                # 5

l[0]                  # 'A'
l[-1]                 # 'E'
# l[10]               # Error

l[:-1]                # ['A', 'B', 'C', 'D'     ]
l[1:]                 # [     'B', 'C', 'D', 'E']
l[2:3]                # [          'C'          ]
l[::-1]               # ['E', 'D', 'C', 'B', 'A']
l[::2]                # ['A',      'C',      'E']

l.append(None)        # ['A', 'B', 'C', 'D', 'E', None]
l.pop()               # ['A', 'B', 'C', 'D', 'E']

l.insert(2, "X")      # ['A', 'B', 'X', 'C', 'D', 'E']
l.pop(2)              # ['A', 'B', 'C', 'D', 'E']

l.extend(["F", "G"])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del l[6]              # ['A', 'B', 'C', 'D', 'E', 'F' ]
l.remove("F")         # ['A', 'B', 'C', 'D', 'E' ]

# TUPLE
tp: tuple = (1,2,3)   # (1, 2, 3)
(a, b, c) = tp        # a=1 | b=2 | c=3

# SET
st = set()
st: set = {"a", "b", "c"}   # {'a', 'b', 'c'}
st.add("a")                 # {'a', 'b', 'c'}
st.add("a")                 # {'a', 'b', 'c'}
st.update(["a", "d"])       # {'a', 'b', 'c', 'd'}
st.discard("x")             # {'a', 'b', 'c', 'd'}
st.discard("d")             # {'a', 'b', 'c'}
st.remove("c")              # {'a', 'b', 'c'}

for x in st:
  x                         # a b

st.clear()                  # set()


# DICTIONARY
dic = {}
dic: dict = {'a': 10, 'b': 20}
dic['a']                  # 10
dic.get('a')              # 10 
dic.get('x', 'default')   # default
dic['a'] = 1              # {'a': 1, 'b': 20}
'a' in dic                # True
'x' in dic                # False

for key in dic:
  f"{key}:{dic[key]}"     # a:10 b:20
