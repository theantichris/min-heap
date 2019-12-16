class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        print("Adding {} to {}.".format(element, self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Restoring the heap property...")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:
                print("swapping {} with {}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {}".format(self.heap_list))

    def retrieve_min(self):
        if self.count == 0:
            print("The heap is empty.")
            return None
        min = self.heap_list[1]
        print("Removing {} from {}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list.pop(self.count)
        self.count -= 1
        print("Last element moved to first: {}".format(self.heap_list))
        return min

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1