# Problem 1: Square Root of an Integer

## Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`

Here is some boilerplate code and test cases to start with:

```python

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
```

------------------------

# Problem 2: Search in a Rotated Sorted Array

## Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example:

Input: nums = `[4,5,6,7,0,1,2], target = 0, Output: 4`

Here is some boilerplate code and test cases to start with:

```python

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
```

------------------------

# Problem 3: Rearrange Array Digits

## Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:

```python
    def rearrange_digits(input_list):
        """
        Rearrange Array Elements so as to form two number such that their sum is maximum.

        Args:
        input_list(list): Input List
        Returns:
        (int),(int): Two maximum sums
        """
        pass

    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
```

------------------------

# Problem 4: Dutch National Flag Problem

## Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:

```python
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
    input_list(list): List to be sorted
    """
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
```

------------------------

# Problem 5: Autocomplete with Tries

## Autocomplete with Tries

Please complete the notebook for this project problem and download it for your submission.

# Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:

* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Give it a try by implementing the `TrieNode` and `Trie` classes below!

```python
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for letter in word:
            if (letter in current_node.children.keys()) is False:
                current_node.insert(letter)
            current_node = current_node.children[letter]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for letter in prefix:
            if (letter in current_node.children) is False:
                return None
            current_node = current_node.children[letter]
            
        return current_node

```

# Finding Suffixes

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

```python
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        def suffix_recur(self, suffix, result):
            for (letter, node) in self.children.items():
                new_suffix = suffix + letter
                if node.is_word:
                    result.append(new_suffix)
                suffix_recur(node, new_suffix, result)
            return
        suffix_recur(self, suffix, result)
        return result

```

# Testing it all out

Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

```python
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
```

```python
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
```

<p>Failed to display Jupyter Widget of type <code>interactive</code>.</p>
<p>
  If you're reading this message in the Jupyter Notebook or JupyterLab Notebook, it may mean
  that the widgets JavaScript is still loading. If this message persists, it
  likely means that the widgets JavaScript library is either not installed or
  not enabled. See the <a href="https://ipywidgets.readthedocs.io/en/stable/user_install.html">Jupyter
  Widgets Documentation</a> for setup instructions.
</p>
<p>
  If you're reading this message in another frontend (for example, a static
  rendering on GitHub or <a href="https://nbviewer.jupyter.org/">NBViewer</a>),
  it may mean that your frontend doesn't currently support widgets.
</p>

------------------------

# Problem 6: Unsorted Integer Array

## Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

**Bonus Challenge**: Is it possible to find the max and min in a single traversal?

```python
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
    ints(list): list of integers containing one or more integers
    """
pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
```

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

------------------------

# Problem 7: Request Routing in a Web Server with a Trie

## HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's [SimpleHTTPRequestHandler](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler) which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

```python
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, ...):
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, ...):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, ...):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, ...):
        # Initialize the node with children as before, plus a handler

    def insert(self, ...):
        # Insert the node as before
```

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

```python
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, ...):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        
    def add_handler(self, ...):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        
    def lookup(self, ...):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
    
    def split_path(self, ...):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
```

## Test Cases

```python
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
```
