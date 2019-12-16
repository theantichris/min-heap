class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        print("Adding {} to {}".format(element, self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Restoring the heap...")
        idx = self.count
        parent_idx = self.get_parent_idx(idx)
        while parent_idx > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[parent_idx]
            if parent > child:
                print("swapping {} with {}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[parent_idx] = child
            idx = parent_idx
        print("Heap Restored: {}".format(self.heap_list))

    def heapify_down(self):
        print("Restoring the heap...")
        idx = 1
        while self.has_child(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx
        print("Heap Restored! {}".format(self.heap_list))

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

    def has_child(self, idx):
        return self.get_left_child_idx(idx) <= self.count

    def get_parent_idx(self, idx):
        return idx // 2

    def get_left_child_idx(self, idx):
        return idx * 2

    def get_right_child_idx(self, idx):
        return idx * 2 + 1

    def get_smaller_child_idx(self, idx):
        left_child_idx = self.get_left_child_idx(idx)
        right_child_idx = self.get_right_child_idx(idx)
        if right_child_idx > self.count:
            print("There is only a left child.")
            return left_child_idx

        left_child = self.heap_list[left_child_idx]
        right_child = self.heap_list[right_child_idx]
        if left_child < right_child:
            print("The left child is smaller.")
            return left_child_idx
        else:
            print("The right child is smaller.")
            return right_child_idx