# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler: str, error_handler: str):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(error_handler)
        self.error_handler = error_handler
        self.insert([], root_handler)

    def insert(self, path_list: list[str], handler: str):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path_item in path_list:
            if (path_item in current_node.children) is False:
                current_node.insert(path_item)
            current_node = current_node.children[path_item]

        current_node.handler = handler
    def find(self, path_list: list[str]):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path_item in path_list:
            if (path_item in current_node.children) is False:
                return self.error_handler
            current_node = current_node.children[path_item]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, default_handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = default_handler
        self.default_handler = default_handler
    def insert(self, value):
        # Insert the node as before
        self.children[value] = RouteTrieNode(self.default_handler)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler: str, error_handler: str):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_handler, error_handler)
    def add_handler(self, path: str, handler: str):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route.insert(path_list, handler)
        
    def lookup(self, path: str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.route.find(path_list)
    
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split("/")
        result =  list(filter(lambda x: x != "" ,path_list))
        return result
    

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

router.add_handler("/home/about/me/1", "detail_handler")
print(router.lookup("/home/about/me/1"))        # detail_handler

router.add_handler("/home/me/1", "short_detail_handler")
print(router.lookup("/home/me/1"))              # short_detail_handler

print(router.lookup(""))                        # root_handler

print(router.lookup("wrong_path"))              # not found handler