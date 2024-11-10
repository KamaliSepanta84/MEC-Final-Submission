
import json

# Exception for when username exists
class userException(Exception):

    def __init__(self,message) -> None:
        self.message = message
        super().__init__(self.message)

# Hash object
# Contains user data
class hashObj:

    # Loading username & password data
    def __init__(self) -> None:

        self.filename = "userData/userData.json"

        with open(self.filename,"r+") as f:
            self.data = json.load(f)
    
    # Check if user exists in database
    def check(self,username:str) -> bool:

        try:
            self.data[username]
            return True
        
        except KeyError:
            return False

    def updateJson(self) -> None:
        with open (self.filename,"w") as f:
            json.dump(self.data,f)

    # Creating new user
    def createUser(self,username:str,password:str) -> None: #Throws userException

        # User does not exist
        if not self.check(username):

            self.data[username] = password
            self.updateJson()

        else:
            raise userException("Username Already Exists")



    def show(self):
        print(self.data)

hashObj_instance = hashObj()