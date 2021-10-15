
#takes in a fuction and triples it
def tripler(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper
