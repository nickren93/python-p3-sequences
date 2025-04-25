#!/usr/bin/env python3

def print_fibonacci(length):
    #pass
    fibonacciList = []
    for num in range(length):
        if num == 0:
            fibonacciList.append(0) 
        elif num == 1:
            fibonacciList.append(1)
        else:
            new_element = fibonacciList[num-2] + fibonacciList[num-1]
            fibonacciList.append(new_element)
            
    print(fibonacciList)