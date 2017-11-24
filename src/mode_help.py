import os

def run(arg):
    path = os.environ['CF_HELPER'] + '/res/help'
    with open(path,'r') as file:
        print(file.read(),end='')
    return True