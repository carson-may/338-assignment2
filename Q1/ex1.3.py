
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
