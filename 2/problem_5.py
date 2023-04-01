import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.strftime("%H:%M %d/%m/%Y", time.gmtime())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = (data + self.timestamp).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_block(self, data):
        if self.head == None:
            new_block = Block(data, "0")
            self.head = new_block
            self.tail = new_block
        else:
            new_block = Block(data, self.tail.hash)
            self.tail.next = new_block
            self.tail = new_block

    def print_block_chain(self):
        current = self.head
        if self.head == None:
            print("Empty blockchain")
        else:
            count = 0
            while current != None:
                print(f"Block no {count}")
                print(f"Timestamp: {current.timestamp}")
                print(f"Data: {current.data}")
                print(f"Hash: {current.hash}")
                print(f"Previous hash: {current.previous_hash}")
                print("---------------------------")
                current = current.next
                count = count + 1

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1

block = Blockchain()
block.add_block("first block")
block.add_block("second block")
block.add_block("third block")
block.print_block_chain()
'''
Block no 0
Timestamp: 17:23 24/03/2023
Data: first block
Hash: 859783c59b1577580a5c943ed58f2508417229c91f7a9c963e02a91a769d2d31
Previous hash: 0
---------------------------
Block no 1
Timestamp: 17:23 24/03/2023
Data: second block
Hash: c4df82989ccebfe7aff1b047e09c52e2a042042090b146abbf6bd6096a181be6
Previous hash: 859783c59b1577580a5c943ed58f2508417229c91f7a9c963e02a91a769d2d31
---------------------------
Block no 2
Timestamp: 17:23 24/03/2023
Data: third block
Hash: 25f99247704c1bb809ec02a9e690fa27caba5646125661ea661dc7598935e60a
Previous hash: c4df82989ccebfe7aff1b047e09c52e2a042042090b146abbf6bd6096a181be6
---------------------------
'''

# Test Case 2
block = Blockchain()            #empty blockchain
block.print_block_chain()
'''
Empty blockchain
'''

# Test Case 3
block = Blockchain()
block.add_block("")             #empty data string
block.print_block_chain()  
'''
Block no 0
Timestamp: 17:27 24/03/2023
Data:
Hash: 300646f2d03271126b67bc23af81b4b03838a6fd6bbbf0655ab239da70ad9aca
Previous hash: 0
---------------------------
'''