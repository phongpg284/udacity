import sys

class Huffman_node:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left_child = None
        self.right_child = None
        self.counter = -1
    def set_counter(self, value): 
        self.counter = value

    def get_value(self):
        return self.value

    def get_frequency(self):
        return self.frequency

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None

class Priority_queue():
    def __init__(self):
        self.list: list[Huffman_node] = list()
        self.size = 0
        self.counter = 0            # add counter to make heap tree stable

    def get_left_child(self, index):
        if index * 2 + 1 < self.size:
            return index * 2 + 1
        return -1 

    def get_right_child(self, index):
        if index * 2 + 2 < self.size:
            return index * 2 + 2
        return -1 
        
    def get_parent(self, index):
        if (index - 1) // 2 >= 0:
            return (index - 1) // 2
        return -1
        
    def min_heapify(self, index: int):
        left_child_index = self.get_left_child(index)
        right_child_index = self.get_right_child(index)
        min_index = index

        # get index of min item in heap
        # add counter compare when same frequency for stability
        if left_child_index > 0:
            left_child_frequency = self.list[left_child_index].frequency
            left_child_counter = self.list[left_child_index].counter
            min_frequency = self.list[min_index].frequency
            min_counter = self.list[min_index].counter
            if left_child_frequency < min_frequency:
                min_index = left_child_index
            elif left_child_frequency == min_frequency and left_child_counter < min_counter:
                min_index = left_child_index
        if right_child_index > 0:
            right_child_frequency = self.list[right_child_index].frequency
            right_child_counter = self.list[right_child_index].counter
            min_frequency = self.list[min_index].frequency
            min_counter = self.list[min_index].counter
            if right_child_frequency < min_frequency:
                min_index = right_child_index
            elif right_child_frequency == min_frequency and right_child_counter < min_counter:
                min_index = right_child_index

        # when violate heap rule
        if min_index != index:
            # swap two node 
            self.list[min_index], self.list[index] = self.list[index], self.list[min_index] 
            self.min_heapify(min_index)
        
    def enqueue(self, item: Huffman_node):
        # add counter to enqueue node
        self.counter += 1
        item.set_counter(self.counter)

        self.size += 1
        self.list.append(item)
        new_item_index = self.size - 1
        for i in range(self.get_parent(new_item_index), -1, -1):
            self.min_heapify(i)

    def deque(self) -> Huffman_node:
        min_item = None
        if (self.size > 0):
            min_item = self.list[0]
            self.size -= 1
            last_item = self.list.pop()
            # another check for edge case 1 node only in queue (size = 0 after pop)
            if (self.size > 0):
                self.list[0] = last_item
                self.min_heapify(0)
        return min_item

# convert string to frequency of letters table
def parse_frequency(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict

def huffman_encoding(data):
    # create frequency table
    frequency_table = parse_frequency(data)

    # create priority queue
    p_queue = Priority_queue()
    for letter, frequency in frequency_table.items():
        p_queue.enqueue(Huffman_node(letter, frequency))

    # create huffman tree
    root = get_huffman_tree(p_queue)
    encode_dict = get_encode_dict_from_huffman_tree(root)
    encode_string = ""

    # single letter only case so root node contain value
    if root != None and root.value != "":
        new_root = Huffman_node("", 0)
        new_left_child = Huffman_node("", 0)
        new_right_child = root
        root = new_root
        root.left_child = new_left_child
        root.right_child = new_right_child
        encode_dict[data[0]] = "1"

    for letter in data:
        encode_string = encode_string + encode_dict[letter]
    return encode_string, root

def get_huffman_tree(p_queue: Priority_queue) -> Huffman_node:
    while p_queue.size > 1:
        print(list(map(lambda x: (x.value, x.frequency), p_queue.list)))
        first_node = p_queue.deque()
        second_node = p_queue.deque()
        combine_frequency = first_node.frequency + second_node.frequency

        new_node = Huffman_node("", combine_frequency)
        new_node.left_child = first_node
        new_node.right_child = second_node

        p_queue.enqueue(new_node)
    root = p_queue.deque()
    return root


def get_encode_dict_from_huffman_tree(root):
    encode_letters = dict()
    if root != None:
        traverse_to_leaf_to_encode(root, "", encode_letters)
    return encode_letters

def traverse_to_leaf_to_encode(node, encode_letter, encode_dict):
    node_value = node.get_value()
    if node_value != "":
        encode_dict[node_value] = encode_letter
    if node.has_left_child():
        traverse_to_leaf_to_encode(
            node.get_left_child(), encode_letter + "0", encode_dict)
    if node.has_right_child():
        traverse_to_leaf_to_encode(
            node.get_right_child(), encode_letter + "1", encode_dict)

def huffman_decoding(data, tree):
    decode_string = ""
    current_node = tree
    for bit in data:
        if bit == "0":
            current_node = current_node.get_left_child()
        else:
            current_node = current_node.get_right_child()
        if current_node.get_value() != "":
            decode_string = decode_string + current_node.get_value()
            current_node = tree
    return decode_string

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

    a_great_sentence = "abcABC"
    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

'''
The size of the data is: 55

The content of the data is: abcABC

The size of the encoded data is: 28

The content of the encoded data is: 1001011101110001

The size of the decoded data is: 55

The content of the encoded data is: abcABC
'''

# Test Case 2

a_great_sentence = "aaaaaaaaaa"
print("The size of the data is: {}\n".format(
    sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = huffman_encoding(a_great_sentence)
print("The size of the encoded data is: {}\n".format(
    sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, tree)
print("The size of the decoded data is: {}\n".format(
    sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))

'''
The size of the data is: 59

The content of the data is: aaaaaaaaaa

The size of the encoded data is: 28

The content of the encoded data is: 1111111111

The size of the decoded data is: 59

The content of the encoded data is: aaaaaaaaaa
'''

# Test Case 3

a_great_sentence = ""
print("The size of the data is: {}\n".format(
    sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = huffman_encoding(a_great_sentence)
print("The content of the encoded data is: {}\n".format(encoded_data))

'''
The size of the data is: 49

The content of the data is:

The content of the encoded data is:
'''
