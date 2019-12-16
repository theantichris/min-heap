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

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying down!")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx
        print("Heap Restored! {}".format(self.heap_list))

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def retrieve_min(self):
        if self.count == 0:
            print("The heap is empty.")
            return None
        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {}".format(self.heap_list))
        self.heapify_down()
        return min

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)

        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]
        if left_child < right_child:
            print("The left child is smaller.")
            return self.left_child_idx(idx)
        else:
            print("The right child is smaller.")
            return self.right_child_idx(idx)