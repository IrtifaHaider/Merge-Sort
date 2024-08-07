def merge_sort(array):
    # Base case: if the array has 1 or fewer elements, it is already sorted
    if len(array) <= 1:
        return
    
     # Find the middle point to divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort both halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Initialize indices for the left, right, and sorted arrays
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the two halves back into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from the left part
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copy any remaining elements from the right part
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# Main part of the script
if __name__ == '__main__':
    # Initialize an empty list to hold the elements
    numbers = []

    # Read the number of elements to be sorted
    n = int(input("Enter number of elements : "))

    # Read the elements and add them to the list
    for i in range(0, n):
        ele = int(input())
        numbers.append(ele)  
    print('Unsorted array: '+ str(numbers))
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))