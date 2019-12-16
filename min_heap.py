class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        print("Adding {} to {}.".format(element, self.heap_list))
        self.count += 1
        self.heap_list.append(element)