# Python3 program to implement Queue using
# two stacks with costly enQueue()
 
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
         
        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
 
        # Push item into self.s1
        self.s1.append(x)
 
        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
 
    # Dequeue an item from the queue
    def deQueue(self):
         
            # if first stack is empty
        if len(self.s1) == 0:
            print("Q is Empty")
        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x
 
# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())







# ###############     Queue

# # Queue implementation in Python

# class Queue:

#     def __init__(self):
#         self.queue = []

#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)

#     # Remove an element
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)

#     # Display  the queue
#     def display(self):
#         print(self.queue)

#     def size(self):
#         return len(self.queue)


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)

# q.display()

# q.dequeue()

# print("After removing an element")
# q.display()