def find_min_property(arr, n):
    # Sort the input array
    arr.sort()
    minP = float('inf')
    
    # Iterate through the sorted array
    for i in range(len(arr) - n + 1):
        # Get the current subarray
        subarr = arr[i:i+n]
        # Calculate the value of property P for this subarray
        P = max(subarr) - min(subarr)
        # Print the subarray and its P value
        print(f"Subarray: {subarr}, P: {P}")
        
        # Update minP if necessary
        if P < minP:
            minP = P
    
    # Return the final result
    return minP

test_arr = [1, 10, 30, 20, 100, 2, 3]
test_n = 3
result = find_min_property(test_arr, test_n)
print(f"Result: {result}")


test_arr = [2, 5, 8, 3]
test_n = 2
result = find_min_property(test_arr, test_n)
print(f"Result: {result}")