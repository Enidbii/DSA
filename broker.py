from stacks import Stack
from myqueue import MyQueue
from node import Node

class Broker:
    def __init__(self):
        #new_node = Node(value)
        #self.created_node = new_node
        self.queue = MyQueue()
        self.stack = Stack()

    def send_to_queue(self, value):
        return self.queue.enqueue(value)
    
    
    def from_queue_to_stack(self):
        #print(self.queue.print_queue())
        my_node = self.queue.dequeue()
        #print("My node value %s" % my_node.value)
        print(self.stack.push(my_node.value))
         
    
    def from_stack_to_queue(self):
        node = self.stack.pop()
        #print(node)
        self.queue.enqueue(value=node)
        #return
        # length = self.stack.height
        # for _ in range(length):
        #     value = self.stack.pop()
        #     self.queue.enqueue(value)
        #     print(self.queue)
    def pop_stack_to_queue(self, k):
        #print(self.stack.size())
        for _ in range(k):
            node = self.stack.pop()
            #print(node)
            self.queue.enqueue(value=node)

    
broker = Broker()
broker.send_to_queue(13)
broker.send_to_queue(14)
broker.send_to_queue(15)
broker.send_to_queue(16)
broker.send_to_queue(17)
broker.send_to_queue(18)
broker.from_queue_to_stack()
broker.from_queue_to_stack()
broker.from_queue_to_stack()
broker.from_queue_to_stack()
broker.from_queue_to_stack()
broker.from_queue_to_stack()
print()
broker.pop_stack_to_queue(4)