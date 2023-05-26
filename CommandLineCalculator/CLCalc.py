import time
import random

def init(length):
    array = []
    for i in range (length):
        array.append(random.randint(0, 100))
    return array

def BubbleSort(array):
    for i in range(len(array)-1):
        for j in range (i + 1, len(array)):
            if array[i] > array [j]:
                array[i], array[j] = array[j], array[i]


def experiment():
    for i in range(0, 11000, 1000):
        print(i)
        a = init(i)
        timeCount = time.time()
        BubbleSort(a)
        timeCount = time.time() - timeCount
        print(timeCount)

experiment()
