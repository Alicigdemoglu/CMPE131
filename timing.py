
import time
# Decorator:: calculate_time
def calculate_time(self):
    begin = time.time()
    #time.sleep(2)
    end = time.time()
    return("Total time " + str(end - begin))
  
# test code  
#print(calculate_time())
