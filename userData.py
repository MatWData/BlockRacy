import hashlib


class User:

    def __init__(self, name, NINumber, postcode):
        self.name = name
        self.NINumber = NINumber
        self.postcode = postcode
        self.personalHash = self.hash()
        self.next = None

    def hash(self):
        #secretWord = input("Enter the secret word: ")
        secretWord = "secret"
        hash_str = f"{self.name}{self.NINumber}{self.postcode}{secretWord}".encode('utf-8')
        return hashlib.sha256(hash_str).hexdigest()
    
    def userIsValid(user):
        # This is just an exmaple of how we can verify users per the requirements of the system. A verification for each vote.

        # This will always return true for now
        personalHash = user.personalHash

        if personalHash == user.hash():
            return True


