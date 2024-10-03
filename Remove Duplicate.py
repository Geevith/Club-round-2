def remove_duplicates(sorted_array):
    array = []
    for element in sorted_array:
        if not array or array[-1] != element:
            array.append(element)
    
    return array

# Example usage
i_array = [2, 3, 4, 4, 6, 7, 7]
o_array = remove_duplicates(i_array)
print(o_array)  
