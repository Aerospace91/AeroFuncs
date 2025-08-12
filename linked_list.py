class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def set_next(self, node):
        self.next = node
    
    def __repr__(self):
        return self.val
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_head(self, val):
        node = Node(val)
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)
    
linked_list = LinkedList()
linked_list.add_to_head(5)
linked_list.add_to_head(10)
linked_list.add_to_head(20)
print(linked_list)