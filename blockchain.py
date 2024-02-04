import hashlib
import userData
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
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_hash = self.get_latest_block().hash
        index = len(self.chain)
        new_block = Block(index, data, previous_hash)

        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calc_hash():
                return False
            if current.previous_hash != previous.calc_hash():
                return False
            
        return True
    
    def create_user(self, name = None, NINumber = None, postcode = None):

        if name == None:
            name = input("Enter your name: ")
            NINumber = input("Enter your National Insurance Number: ")
            postcode = input("Enter your postcode: ")

        user = userData.User(name, NINumber, postcode)
        return user
    
    def create_vote(self, user, issueNumber, vote):

        if userData.userIsValid(user) == False:
            print("User is not valid")
            return

        vote_data = {
            "voter": user,
            "issueNumber": issueNumber,
            "vote": vote
        }

        self.add_block(vote_data)


    
