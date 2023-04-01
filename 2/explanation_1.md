In this problem, we need a LRU Cache with 2 requirements:
1. `get()` and `set()` method, both must take `O(1)` time
2. add new item with `set()`, when full capacity we need to remove least recently used item first, then insert new item after

For each requirement, we implement as following:
1. We need a `Hashmap` to store data to fullfil `O(1)` for `get` and `set` action
2. We also need to store data as a `Queue` to fullfil `O(1)` for `set` method when capacity is full

Therefore, for class `LRU_Cache`:
- we have a double linked list `queue` to store data, each item is a `Node` with `key`-`value` when call `set(key, value)`
- and a dictionary `hash_map` with `key`-`value` are `key` and respective `Node` in the queue

Time complexity is guaranteed to be O(1).

For space complexity:
Given n is our cache capacity input `hash_map` dictionary and `queue` implement by linked list will take O(n).