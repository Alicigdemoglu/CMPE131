import time
# calculate the time to run the program
def calculate_time(func):
    def wrapper():
        start = time.time()
        time.sleep(func)
        end = time.time()
        print("Total time ",end - start)
    return wrapper
