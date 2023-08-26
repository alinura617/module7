# Alinura Sultanova
# 08.17.2023

# Problem 4: Write a Python function that takes a list of numbers and returns a new list with
unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append
function

def uniqueElementsList(input_list):
    """
    Creates a new list with unique elements from a given list.
    
    Parameters:
    input_list (list): List containing elements with possible duplicates.
    
    Returns:
    list: A new list containing unique elements from the input list.
    """
    unique_list = []  # Initialize an empty list to store unique elements
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)  # Add the element to the unique list if not already present
    
    return unique_list

# Test the function
numbers = [1, 3, 3, 3, 6, 2, 3, 5]
unique_numbers = uniqueElementsList(numbers)
print("Original list:", numbers)
print("List with unique elements:", unique_numbers)

# finish