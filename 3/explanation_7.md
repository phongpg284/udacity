Given n is average length of keys

- For class `RouteTrieNode`: we have only `insert()` method with `O(1)` for both time complexity and space complexity
  - `init` will take `O(1)`
- For class `RouteTrie`:
  - `init` also take `O(1)` to init root node and error handler
  - `insert()` will need to traverse each node for each letter, complexity will be `O(n)` for both time and space complexity
  - `find()` will need to traverse the same, so complextity will be `O(n)` for time complexity and `O(1)` only for space complexity

- For class `Router`:
  - `init` take `O(1)` to init self.route
  - `add_handler()` call route `insert()` so it will take `O(n)` complexity for both space and time
  - `lookup()` call route `find()` so it will be `O(n)` and `O(1)` for time and space complexity
  - `split_path()` will be `O(n)` for both time and space complexity given `n` is string length
