from sys import getrecursionlimit, setrecursionlimit
getrecursionlimit() # 1000
setrecursionlimit(2000)

def countdown(n):
  print(n)
  if n == 0:
      return             # Terminate recursion
  else:
      countdown(n - 1)   # Recursive call
    
countdown(5)


def factorial(n):
  print(f"factorial() called with n = {n}")
  return_value = 1 if n <= 1 else n * factorial(n - 1)
  print(f"-> factorial({n}) returns {return_value}")
  return return_value

factorial(4)