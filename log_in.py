import userObj
from argon2 import *
from hashlib import *


def log_in(user_name, password):
    user = userObj.hashObj_instance

    try:
        my_user = user.data[user_name]
        my_salt = my_user["Salt"]
        stored_hashed_password =  my_user["Hashed_Password"]

    # In case user does not exist
    except KeyError:
        raise userObj.userException(1)

    try:
        ph = PasswordHasher(time_cost= 6 , memory_cost= 4096)
        ph.verify(stored_hashed_password , password + my_salt)
        return True
    except:
        return False


