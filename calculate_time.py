# Import time
import time
# Decorator:: calculate_time
def calculate_time():
    begin = time.time()
    #time.sleep(2)
    end = time.time()
    print("Total time ",end - begin)
  
# Driver code  
calculate_time()