import useChain

chain = useChain.useChain()

for block in chain.chain.chain:
    print("Block Index: ", block.index)
    print("Timestamp: ", block.timestamp)
    print("Data: ", block.data)
    print("Previous Hash: ", block.previous_hash)
    print("Hash: ", block.hash)
    print("=====================================")
    print("\n")



