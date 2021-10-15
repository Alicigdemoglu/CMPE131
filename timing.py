
import time
# Decorator:: calculate_time
def calculate_time(func):
    def wrapper():
        start = time.time()
        #time.sleep(2)
        end = time.time()
        print("Total time ",end - start)
    return wrapper
