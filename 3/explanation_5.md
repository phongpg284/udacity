Given n is average length of keys
m is alphabet size

- For class `TrieNode`:
  - `init` will take `O(1)` for both time and space complexity.
  - `insert()` method with `O(1)` for both time complexity and space complexity
  - For `suffixes()` method, time and space complexity will be `O(m * n)`.

- For class `Trie`:
  - `init` only create root node so will take `O(1)`
  - `insert()` will need to traverse each node for each letter, complexity will be `O(n)` for both time and space complexity
  - `find()` will need to traverse the same, so complextity will be `O(n)` for time complexity and `O(1)` only for space complexity
