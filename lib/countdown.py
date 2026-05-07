# your code goes here!# 

from time import time

import time # Use the whole module to access time.sleep()

def countdown(n):
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    while n > 0:
        print(f"{n} SECOND(S)!")
        time.sleep(1)
        n -= 1
    print("HAPPY NEW YEAR!")
