
import json
import log_in
import sign_up

# Exception for when username exists
class userException(Exception):

    def __init__(self,messageType) -> None:

        message = ""

        match messageType:
            case 1: message = "User Does Not Exist"
            case 2: message = "User Already Exists"
            case 3: message = "Password is Incorrect"
            case 4: message = "Username is Taken"

        self.message = message
        super().__init__(self.message)

# Hash object
# Contains user data
class userObj:

    # Loading username & password data
    def __init__(self) -> None:

        self.filename = "userData.json"

        with open(self.filename,"r+") as f:
            self.data = json.load(f)
    
    # Check if user exists in database
    def exists(self,username:str) -> bool:

        try:
            self.data[username]
            return True
        
        except KeyError:
            return False

    # Update user data json file
    def updateJson(self) -> None:
        with open (self.filename,"w") as f:
            json.dump(self.data,f,indent=4)

    # Creating new user
    def createUser(self,username:str,encrypted_dictionary:str) -> None: #Throws userException

        # User does not exist
        if not self.exists(username):

            # Appending data to json
            self.data[username] = encrypted_dictionary
            self.updateJson()

        # User exists
        else:
            raise userException(2)

    # Checks if user credentials are valid
    def check(self,username:str,password:str) -> bool: #Throws userException

        # User exists
        if self.exists(username):
            return self.data[username]["Hashed_Password"] == password
        
        # User does not exist
        else:
            raise userException(1)

    # Update user password
    def updatePassword(self,username:str,password:str,newPassword:str) -> None: #Throws userException

        # User exists
        if self.exists(username):

            # User password is correct
            if self.data[username] == password:
                self.data[username] = newPassword
                self.updateJson()

            # User password is incorrect
            else:
                raise userException(3)
        
        # User does not exist
        else:
            raise userException(1)

    # Update user's username
    def updateUsername(self, username:str, newUsername:str, password:str) -> None: #Throws Exception

        # If user exists
        if self.exists(username):


            # Username is taken
            if self.exists(newUsername):
                raise userException(4)
            
            # Username is not taken
            else:

                # If user entered proper login
                if self.data[username] == password:
                    # Renaming user
                    self.data[newUsername] = self.data.pop(username)
                    self.updateJson()

                # User didn't enter proper login
                else:
                    raise userException(3)
            
        # User does not exist
        else:
            raise userException(1)

    # Backdoor access to database
    def __show(self):
        print(self.data)

# Create instance of object
hashObj_instance = userObj()