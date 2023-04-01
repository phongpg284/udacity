For `union()` function, we create a dictionary and iterate through 2 linked list and add each item to our dictionary, then get dictionary.keys() and convert back to link list
For `intersection()` function, we create 1 temp dictionary to add all item from linkedlist 1, then iterate and check if any item from temp dictionary appear in linkedlist 2, if yes add to final intersection dictionary.
We use `dictionary` instead `set` for training since `set` already have `union()` and `intersection()`.

We need 2 loop to iterate through 2 linked list, therefore the complexity will be O(m + n) with m, n length of 2 linked list input for both `union()` and `intersection()`.

---------------------------------------------------------------------------------------------------------------------------------------------

For 2 linkedlist with length m, n; space complexity will be O(m + n) given n is number of blocks.
During `union()` and `intersection()`, we create some temporary or result dictionaries but the space complexity will still be constant * (m + n)
Therefore final space complexity will be O(m + n)
