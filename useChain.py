import blockchain
import userData




# Test the code
chain = blockchain.Blockchain()


user1 = chain.create_user("John Doe","AB123456C", "AB1 2CD")
user2 = chain.create_user("Jane Doe", "CD123456A", "CD3 4EF")
user3 = chain.create_user("John Smith", "EF123456B", "EF5 6GH")

chain.create_vote(user1, 1, "yes")
chain.create_vote(user2, 1, "no")
chain.create_vote(user3, 1, "yes")

for block in chain.chain:
    print("Block Index: ", block.index)
    print("Timestamp: ", block.timestamp)
    print("Data: ", block.data)
    print("Previous Hash: ", block.previous_hash)
    print("Hash: ", block.hash)
    print("=====================================")
    print("\n")