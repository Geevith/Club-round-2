class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
if __name__ == "__main__":
    my_stack = Stack()
    
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    
    print("Top item:", my_stack.peek())  
    print("Stack size:", my_stack.size())  

    print("Popped item:", my_stack.pop())  
    print("Stack size after pop:", my_stack.size())  

    print("Top item after pop:", my_stack.peek())  
