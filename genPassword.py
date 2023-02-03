import random 
import string

def generatePassword(par):
    # splitting params into each cat 
    params = eval(par)
    length = params['len']
    cap = params['upper']
    special = params['spChar']
    num = params['num']

    password = random.choice(string.ascii_lowercase)

    # list of characters
    choices = string.ascii_lowercase

    if cap:
        choices += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)
    if special:
        choices += string.punctuation
        password += random.choice(string.punctuation)
    if num:
        choices += string.digits
        password += random.choice(string.digits)

    #generage and verify
    while len(password) < length:
        password += random.choice(choices)

    return ''.join(random.sample(password,len(password)))

