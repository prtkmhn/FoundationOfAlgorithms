def find_minimum_property(sorted_array, subarray_size):
    sorted_array.sort()
    
    for index in range(len(sorted_array) - subarray_size + 1):
        current_subarray = sorted_array[index:index+subarray_size]
        property_value = max(current_subarray) - min(current_subarray)
        print("Subarray:", current_subarray)
        print("P:", property_value)
        
        if index == 0:
            min_property = property_value
        elif property_value < min_property:
            min_property = property_value
    
    return min_property

test_array = [2, 5, 8, 3] 
subarray_size = 2
result = find_minimum_property(test_array, subarray_size)
print("Result:", result)