import hashlib
import userData
import pickle
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        # Include the block data in the hash calculation
        hash_str = "{}{}{}".format(self.timestamp, self.data, self.previous_hash).encode('utf-8')
        return hashlib.sha256(hash_str).hexdigest()

class Blockchain:

    def __init__(self):
        self.chain = self.load_chain()
        self.save_chain()
    
    def load_chain(self):
        try:
            with open("blockchain.pkl", "rb") as f:
                return pickle.load(f)
            
        except FileNotFoundError:
            print("No chain found. Creating a new one")
            return [self.create_genesis_block()]
    
    def save_chain(self):
        with open("blockchain.pkl", "wb") as f:
            pickle.dump(self.chain, f)
    
    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "We Have To Save Democracy")
        return genesis_block
    
    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_hash = self.get_latest_block().hash
        index = len(self.chain)
        new_block = Block(index, data, previous_hash)
        self.chain.append(new_block)
        self.save_chain()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calc_hash():
                return False
            if current.previous_hash != previous.calc_hash():
                return False
            
        return True
    
    
    


    
