

def generatePassword(par):
    # splitting params into each cat 
    params = eval(par)
    len = params['len']
    cap = params['upper']
    special = params['spChar']


    return str(type(len)) + str(type(cap)) + str(type(special))