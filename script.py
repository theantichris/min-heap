# importing heap class
from min_heap import MinHeap 

# an instance of MinHeap to use
min_heap = MinHeap()

# the internal list for our example
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
print(min_heap.heap_list)

# example of how to use the helper methods:
print("the parent index of 4 is:")
print(min_heap.parent_idx(4))
print("the left child index of 3 is:")
print(min_heap.left_child_idx(3))

idx_2_left_child_idx = min_heap.left_child_idx(2)
print("The left child index of index 2 is:")
print(idx_2_left_child_idx)
print("The left child element of index 2 is:")
print(min_heap.heap_list[idx_2_left_child_idx])

idx_3_parent_idx = min_heap.parent_idx(3)
print("The parent index of index 3 is:")
print(idx_3_parent_idx)
print("The parent element of index 3 is:")
print(min_heap.heap_list[idx_3_parent_idx])

idx_3_right_child_idx = min_heap.right_child_idx(3)
print("The right child index of index 3 is:")
print(idx_3_right_child_idx)
print("The right child element of index 3 is:")
print(min_heap.heap_list[idx_3_right_child_idx])
