# Alinura Sultanova
# 08.17.2023

#Problem 2: Write a Python function to check whether a number is in a given range. Use
range(1,10). Print whether the number is in or not in the range

def checkNumberInRange(number):
    """
    Checks if a given number is within the range of 1 to 10.
    
    Parameters:
    number (int): The number to be checked.
    
    Returns:
    str: A message indicating whether the number is in the range or not.
    """
    if 1 <= number <= 10:  # Check if the number is within the specified range
        return "The number is in the range."
    else:
        return "The number is not in the range."

# Test the function
test_number = 7
result_message = checkNumberInRange(test_number)
print(result_message)

# finish