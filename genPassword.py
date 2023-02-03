import random 
import string

def generatePassword(par):
    # splitting params into each cat 
    params = eval(par)
    length = params['len']
    cap = params['upper']
    special = params['spChar']
    num = params['num']

    password = ""

    # list of characters
    choices = string.ascii_lowercase

    if cap:
        choices += string.ascii_uppercase
    if special:
        choices += string.punctuation
    if num:
        choices += string.digits

    for x in range(length):    
        password += random.choice(choices)

    return password