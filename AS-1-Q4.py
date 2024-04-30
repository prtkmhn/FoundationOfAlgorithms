import random
import time
from datetime import datetime

def find_max_index(A):
    max_index = 0
    for i in range(len(A)):
        if A[i] is not None and (A[max_index] is None or A[i] > A[max_index]):
            max_index = i
    return max_index

def sort_array(A):
    n = len(A)
    B = [None] * n
    for i in range(n):
        max_index = find_max_index(A)
        B[n - i - 1] = A[max_index]
        A[max_index] = None
    return B

def main():
    n = int(input("Enter a number between 0 and 999: "))
    A = [random.randint(0, 999) for i in range(n)]
    
    start_time = datetime.now()
    B = sort_array(A)
    end_time = datetime.now()
    
    print("Sorted array:", B)
    print("Time taken:", (end_time - start_time) * 1000, "milliseconds")

if __name__ == "__main__":
    main()
