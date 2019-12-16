from random import randrange
from min_heap import MinHeap 

min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  min_heap.add(el)

# test it out, is the minimum number at index 1?
print(min_heap.heap_list)
