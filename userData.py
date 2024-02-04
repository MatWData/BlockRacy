import random
import hashlib


class User:

    def __init__(self, name, NINumber, postcode):
        self.name = name
        self.NINumber = NINumber
        self.postcode = postcode
        self.personalHash = self.hash()
        self.uid = self.hash(True)
        self.next = None

    def hash(self, uniqueID=False):
        #secretWord = input("Enter the secret word: ")
        if uniqueID == False:
            secretWord = self.getSecretWord()
            secretWordString = secretWord[0] + secretWord[1] + secretWord[2]

            hash_str = f"{self.name}{self.NINumber}{self.postcode}{secretWordString}".encode('utf-8')

            return hashlib.sha256(hash_str).hexdigest()
        else:
            secretWord = self.getSecretWord(True)
            hash_str = f"{self.NINumber}{secretWord}".encode('utf-8')
            return hashlib.sha256(hash_str).hexdigest()
    
    def userIsValid(user):
        # This is just an exmaple of how we can verify users per the requirements of the system. A verification for each vote that is made that will be checked against the blockchain, a check for the user's personal hash and a check to see if they've only made one vote.

        # This will always return true for now
        personalHash = user.personalHash



        if user.name == "John Doe":
            return False


    def getSecretWord(self, uid=False):
        word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "xigua", "yuzu", "bottle", "candle", "door", "elephant", "frog", "giraffe", "hat", "igloo", "jacket", "kangaroo", "lion", "monkey", "nose", "octopus", "penguin", "quilt", "rabbit", "snake", "tiger", "umbrella", "vase", "whale", "xylophone", "yak", "zebra", "marvel", "dc", "image", "darkhorse", "valiant", "idw", "boom", "archie", "dynamite", "topcow", "zenescope", "aspen", "avatar", "red5", "onipress", "titan", "aftershock", "blackmask"]

        if uid == False:
            secret_phrase = []
            for i in range(3):
                word = word_list[random.randint(0, len(word_list) - 1)]
                secret_phrase.append(word)
        
        else:
            secret_phrase = "abcdefghiJkl"

        return secret_phrase