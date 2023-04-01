class LRU_Cache(object):
    def __init__(self, capacity):
        self.hash_map = dict()
        self.queue = Queue()
        self.capacity = capacity
        self.size = 0

    def empty(self):
        self.size = 0
        self.hash_map = dict()
        self.queue = Queue()

    def get(self, key):
        node = self.hash_map.get(key)
        if node == None:
            return -1
        
        value = node.get_value()
        self.queue.mark_used_node(node)
        # Retrieve item from provided key. Return -1 if nonexistent.
        return value

    def set(self, key, value):
        is_key_exist = self.hash_map.get(key) != None
        is_full_capacity = self.size == self.capacity

        if is_key_exist == True:
            self.hash_map.get(key).set_value(value) 
        if is_key_exist == False:
            if is_full_capacity:
                delete_item = self.queue.dequeue()
                self.hash_map.pop(delete_item.key)
                self.size = self.size - 1

            new_node = Node(key, value) 
            self.queue.enqueue(new_node)
            self.hash_map[key] = new_node
            self.size = self.size + 1

class Node: 
    def __init__(self, key, value):
        self.key: int = key
        self.value: int = value
        self.next: Node = None
        self.prev: Node = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
    
    def enqueue(self, node: Node):
        if self.tail == None: 
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        node.next = None
    
    def dequeue(self):
        pop_item = self.head
        if pop_item != None:
            self.head = pop_item.next
            self.head.prev = None
        return pop_item
    
    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        if node == self.head:
            self.head = next_node
        if node == self.tail:
            self.tail = prev_node
        if prev_node != None:
            prev_node.next = next_node
        if next_node != None:
            next_node.prev = prev_node
        
    def mark_used_node(self, used_node: Node):
        self.remove(used_node)
        self.enqueue(used_node)


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
def assert_test_one():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))         # return 1
    print(our_cache.get(2))         # return 2
    print(our_cache.get(9))         # return -1
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))         # return -1 

assert_test_one()

# Test Case 2

def assert_test_two():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    print(our_cache.get(1))         # return 1

    our_cache.set(1, 2)
    print(our_cache.get(1))         # return 2 cause rewrite cache

    our_cache.set(1, 3)
    print(our_cache.get(1))         # return 3 cause rewrite cache

    our_cache.set(2, 2)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    our_cache.set(7, 7)
    print(our_cache.get(1))         # return -1 

assert_test_two()

# Test Case 3
def assert_test_three():
    our_cache = LRU_Cache(5)        # empty cache
    print(our_cache.get(1))         # return -1
    print(our_cache.get(2))         # return -1
    print(our_cache.get(9))         # return -1

assert_test_three()