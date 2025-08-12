from typing import Any, Optional

class Stack:
    """A simple stack (Last-In, First-Out) data structure"""
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self.items: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Push an item onto the top of the stack.
        
        Args:
            item (Any): The item to be added to the stack
            
        Example:
            >>> s = Stack()
            >>> s.push(10)
            >>> s.push(20)
            >>> s.peek()
            20
        """
        self.items.append(item)
        
    def size(self) -> int:
        """
        Get the number of items currently in the stack.
        
        Returns:
            int: The number of elements in the stack
        """
        return len(self.items)
    
    def peek(self) -> Optional[Any]:
        """
        View the item at the top of the stack without removing it.
        
        Returns:
            Any or None: The top item if the stack is not empty, otherwise None
        """
        if len(self.items) > 0:
            return self.items[-1]
        return None
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return the item at the top of the stack.
        
        Returns:
            Any or None: The removed item, or None if the stack is empty.
        """
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item
    
class Queue:
    def __init__(self) -> None:
        """Initialize an empty queue."""
        self.items = []
    
    def push(self, item: Any) -> None:
        """
        Push an item onto the back of the queue.
        
        Args:
            item (Any): The item to be added to the queue
            
        Example:
            >>> s = Queue()
            >>> s.push(10)
            >>> s.push(20)
            >>> s.peek()
            10
        """
        self.items.insert(0, item)
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return the item at the front of the queue.
        
        Returns:
            Any or None: The removed item, or None if the queue is empty.
        """
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp
    
    def peek(self) -> Optional[Any]:
        """
        View the item at the front of the queue without removing it.
        
        Returns:
            Any or None: The top item if the queue is not empty, otherwise None
        """
        if len(self.items) == 0:
            return None
        return self.items[-1]
    
    def size(self) -> int:
        """
        Get the number of items currently in the queue.
        
        Returns:
            int: The number of elements in the queue
        """
        return len(self.items)