For this problem, we will walk through each step:
- First we need to convert from input string to a dictionary with `key-value` as `letter` and `frequency` like `{"A" : 4}`
- Then we need a class `Priority_queue`, implement by a `Min Heap`, so we can move the dictionary above into it to get a Priority queue
- After that we convert to Huffman tree contain `Huffman_node`
- Finally parsing from Huffman tree to code for each letter by traverse from root to each leaf
- For some edge case, like when multiple letter with same frequency `1`, priority queue implement by min heap is not stable, therefore we will add `counter` to Huffman node to compare when heapify.

Let say n is number of distinct letter from input string
By implement Min Heap for Priority Queue, complexity for this queue will be O(log n) for both `enque()` and `deque()`
For the Huffman Tree, complexity will be O(n log n) to build the tree, because each operation to build 1 node require log(n) from `deque()` and `enque()`
Traverse through the tree to get code for n letter will have complexity of O(n log n)
Therefore complexity for encoding will be O(n log n)

For decoding, complexity will be O(n) give n is input encoded string length

--------------------------------------------------------------------------------
Space complexity will be O(n) given n is number of letters.