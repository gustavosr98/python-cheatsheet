print("SORTING")
a = list(map(int, input("Enter array to sort. Ej. 7 5 6 1 9: ").split()))

def selection(a: list) -> list:
  """
  Selection Sort
  https://www.youtube.com/watch?v=g-PGLbMth_g&ab_channel=MichaelSambol
  """

  for i in range(len(a)):
    min = i
    for j in range(i, len(a)):
      if ( a[j] < a[i] ): min = j
    a[i] , a[min] = a[min] , a[i]

  return a

print("selection: ", selection(a))