import json
import matplotlib.pyplot as plt
import sys
import timeit
import math
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    with open("Q2/ex2.5.json") as a:
        input = json.load(a)
    time_series = []
    for arr in input:
        time = timeit.repeat('func1(arr_cpy, 0, len(arr_cpy)-1)',
                        setup='arr_cpy = arr[:]',
                        globals = {'arr':arr, 'func1':func1},
                        repeat=10,
                        number=1)
        print('test')
        time_series.append(sum(time)/len(time))
    x = [x for x in range(1000, 10000)]
    y = [0.0000002*i*math.log(i, 10) for i in x]
    n = [len(arr) for arr in input]
    plt.plot(x, y, label='nlog(n)')
    plt.plot(n, time_series, label='measured data')
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()