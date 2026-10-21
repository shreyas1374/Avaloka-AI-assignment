
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add_to_front(node)

        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.add_to_front(node)
            return

        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add_to_front(new_node)

lru = LRUCache(2)

lru.put(1, 10)
lru.put(2, 20)

print(lru.get(1))  # 10

lru.put(3, 30)
print(lru.get(2))  # -1

lru.put(4, 40)
print(lru.get(1))  # -1
print(lru.get(3))  # 30
print(lru.get(4))  # 40
