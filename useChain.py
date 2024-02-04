import blockchain
import userData
import pickle


class useChain:
    def __init__(self):
        self.chain = blockchain.Blockchain()
        self.users = self.load_users()
        print(self.users)
    
    def load_users(self):
        try:
            with open("users.pkl", "rb") as f:
                return pickle.load(f)
            
        except FileNotFoundError:
            print("No users yet.")
            return set()
    
    def save_users(self):
        with open("users.pkl", "wb") as f:
            pickle.dump(self.users, f)
    
    def create_user(self, name, NINumber, postcode):
        user = userData.User(name, NINumber, postcode)
        uid = user.uid
        

        for existing_user in self.users:
            if existing_user[1] == uid:
                print("User already exists")
                return None
        
        user_info = (user.personalHash, uid)
        self.users.add(user_info)
        self.save_users()
        return user
    
    def create_vote(self, user, issueNumber, vote):

        if user is None:
            return

        vote_data = {
            "voter": user.personalHash,
            "issueNumber": issueNumber,
            "vote": vote
        }

        self.chain.add_block(vote_data)

