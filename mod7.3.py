# Alinura Sultanova
# 08.17.2023

#Problem 3: Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7,
-1]

def multiplyListNumbers(numbers_list):
    """
    Multiplies all the numbers in a given list.
    
    Parameters:
    numbers_list (list): List containing numbers to be multiplied.
    
    Returns:
    int: The result of multiplying all the numbers in the list.
    """
    result = 1
    for number in numbers_list:
        result *= number  # Multiply each number with the previous result
    
    return result

# Test the function
numbers = [5, 2, 7, -1]
result = multiplyListNumbers(numbers)
print("The product of the numbers in the list is:", result)

# finish