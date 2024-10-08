#!/usr/bin/python3 env

class MaxHeap:
    def __init__(self):
        """
        creates heap list
        """
        self.heap = []

    def _left_child(self, index):
        """
        :param index: parent's index
        :return: index of the left child
        """
        return 2 * index + 1
    def _right_child(self, index):
        """
        :param index:parent's index
        :return: index of right child
        """
        return 2 * index + 2

    def _parent(self, index):
        """
        :param index: child's index
        :return: parent's index
        """
        return (index - 1) // 2
    def swap(self, index1, index2):
        """
        swaps value at index1 with value at index2
        :param index1: first index
        :param index2: second index
        :return: Nothing
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self,value):
        """
        inserts into the heap
        :param value: value to insert
        :return: heap
        """
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self.swap(current, self._parent(current))
            #update current
            current = self._parent(current)

    def sink_down(self, index):
        """
        balances the heap
        :param index:index
        :return:Nothing
        """
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return



    def remove(self):
        """
        removes value from top of the heap
        :return: removed value
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return max_value


heapy = MaxHeap()
heapy.insert(99)
heapy.insert(75)
heapy.insert(80)
heapy.insert(55)
heapy.insert(50)
heapy.insert(60)
heapy.insert(100)
print(heapy.heap)
heapy.remove()
print(heapy.heap)
heapy.remove()
print(heapy.heap)