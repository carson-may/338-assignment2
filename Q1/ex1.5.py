import timeit
import matplotlib.pyplot as plt
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


memory = {0:0, 1:1} # Store base cases
def funcMem(n):
    if n == 0:
        return memory[0] # 0
    elif n == 1:
        return memory[1] # 1
    else:
        if n not in memory.keys():
            i = funcMem(n - 1) + funcMem(n - 2)
            memory[n] = i # store the nth fib number
        else:
            i = memory[n]
        return i    

def main():
    recursiveTime = {}
    memoTime = {}
    for i in range(0, 36):
        timeRecursion = timeit.timeit('func(i)',
                             globals= {'func':func, 'i': i},
                             number=1)
        timeMemo = timeit.timeit('funcMem(i)',
                                globals= {'memory':memory, 'funcMem':funcMem, 'i':i },
                                number= 1)
        recursiveTime[i] = timeRecursion
        memoTime[i] = timeMemo
    x = memoTime.keys()
    recursY = recursiveTime.values()
    memoY = memoTime.values()
    plt.plot(x , recursY, label='Recursive Function T(2^n)')
    plt.plot(x, memoY, label="Memoization Function T(n)")
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
