import os
from time import sleep
import random

# isso foi feito no dedo ta
# so ta em ingles por costume

def is_even(n):
    return n%2 == 0

def collatz_conjecture(x):
    while(x > 1):
        if is_even(x):
            x = x/2
        else:
            x = 3 * x + 1
        print(f"is even {is_even(x)} -> {x}")

def main():
    n = int(input("number of process to create: "))
    
    child = []

    for _ in range(n):
        print("     proc create")
        c = os.fork()
        
        if c != 0:
            child.append(c)

        # child
        if c == 0:
            print(f"im child {c}")
            # cp = os.getpid()
            # collatz_conjecture(2)
            
            sleep(0.5)

    for pid in child:
        print(f"\nwaiting child {pid}")
        x = os.waitpid(pid, 0)
        print(f"child {x[0]} end")
        


main()