#!/usr/bin/python3 env
"""creating stacks and ques udsing lists"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    def size(self):
        return len(self.stack_list)
    def push(self, value):
        self.stacklist.append(value)
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

class Queue:
    def __init__(self):
        self.queue_list = []

    def print_queue(self):
        for i in range(len(self.queue_list)-1,