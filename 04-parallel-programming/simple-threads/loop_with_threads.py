import threading
import random
from time import sleep, ctime


def task1():
    for i in range(10):
        print("T1 " + str(i), flush=True)
        sleep(random.randint(1, 5))

def task2():
    for i in range(10):
        print("T2 " + str(i), flush=True)
        sleep(random.randint(1, 5))

print("Starting at: ", ctime())
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Ending at: ", ctime())
