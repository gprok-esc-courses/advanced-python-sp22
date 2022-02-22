from time import sleep, ctime


def task1():
    for i in range(10):
        print("T1", i)
        sleep(2)

def task2():
    for i in range(10):
        print("T2", i)
        sleep(2)


print("Starting at: ", ctime())
task1()
task2()
print("Ending at: ", ctime())
