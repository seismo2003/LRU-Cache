#Create a double linkedlist
class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        node.next = None
        node.prev = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = {}
        self.num_of_entries = 0
        self.head = None
        self.tail = None
        self.capacity = capacity



    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hash_map:
            return -1
        else:
            former_node = self.hash_map[key].prev
            latter_node = self.hash_map[key].next
            #if the key is calling for the last node
            if former_node != None and latter_node is None:
                former_node.next = latter_node
                self.tail = former_node
                current_head = self.head
                self.head = self.hash_map[key]
                self.head.next = current_head
                current_head.prev = self.head
                self.head.prev = None
            #if the key calls for the middle node
            elif former_node != None and latter_node != None:
                former_node.next = latter_node
                latter_node.prev = former_node
                current_head = self.head
                self.head = self.hash_map[key]
                self.head.next = current_head
                current_head.prev = self.head
                self.head.prev = None
            #if the key calls for the first node, then there's no position switching needed
            return self.hash_map[key].value



    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if self.capacity <= 0:
            return -1

        current_mode = self.head
        new_node = LinkedListNode(key, value)

        #if there's nothing in the linkedlist
        if current_mode == None:
            self.hash_map[key] = new_node
            self.num_of_entries += 1
            self.head = self.hash_map[key]
            self.tail = self.hash_map[key]
        else:
        #if the key node does not exist
            if key not in self.hash_map:
                self.hash_map[key] = new_node
                self.head = self.hash_map[key]
                self.head.next = current_mode
                current_mode.prev = self.head
                self.num_of_entries += 1
            #if the key node exists
            else:
                former_node = self.hash_map[key].prev
                latter_node = self.hash_map[key].next
                # if the target node is the last node
                if former_node != None and latter_node is None:
                    former_node.next = latter_node
                    self.tail = former_node
                    self.hash_map[key] = new_node
                    self.head = self.hash_map[key]
                    current_mode.prev = self.head
                    self.head.next = current_mode
                # if the target node is in the middle node
                elif former_node != None and latter_node != None:
                    former_node.next = latter_node
                    latter_node.prev = former_node
                    self.tail = former_node
                    self.hash_map[key] = new_node
                    self.head = self.hash_map[key]
                    current_mode.prev = self.head
                    self.head.next = current_mode
                elif former_node == None:
                    # if the target node is the first node
                    self.hash_map[key] = new_node
                    self.head = self.hash_map[key]
                    self.head.next = current_mode.next


        if self.num_of_entries > self.capacity:
            current_tail = self.tail
            key = current_tail.key
            self.tail = self.tail.prev
            self.tail.next = None
            del self.hash_map[key]
            self.num_of_entries -= 1



#Edge Test Cases:
our_cache=LRU_Cache(0)
our_cache.set(1,1)
print(our_cache.get(1))
our_cache.set(2,2)
print(our_cache.get(2))
our_cache.get(1)

our_cache=LRU_Cache(-5)
our_cache.set(1,1)
print(our_cache.get(1))
our_cache.set(2,2)
print(our_cache.get(2))
our_cache.get(1)

#Normal Test cases
our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
our_cache.get(4)   # Expected Value = 4
print(our_cache.get(4))
our_cache.get(1)   # Expected Value = -1
print(our_cache.get(1))
our_cache.set(2,7)
print(our_cache.get(2))
