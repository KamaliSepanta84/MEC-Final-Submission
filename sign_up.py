from argon2 import *
from hashlib import *
import os
import userObj


def sign_up(user_name , password):
    try:
        user = userObj.hashObj_instance

        user_name = user_name
        password = password
        encryption_dictionary = encrypt(user_name, password)    

        user.createUser(user_name,encryption_dictionary)

    except userObj.userException as userException:
        raise userException

    
def encrypt(user_name , password):
    new_dictionary = {}
    salt = custom_salt(user_name)
    user_hashed_password = hash_password(password,salt)
    new_dictionary["Hashed_Password"] = user_hashed_password
    new_dictionary["Salt"] = salt
    return new_dictionary


def hash_password(user_password: str, salt: str) -> str:
    ph = PasswordHasher(time_cost= 6 , memory_cost= 4096)
    password = user_password
    hashed_password = ph.hash(password + salt)
    return hashed_password


def custom_salt(user_name:str) -> str:
    random_value = os.urandom(16)
    generated_salt = sha256(user_name.encode() + random_value).hexdigest()
    return generated_salt






