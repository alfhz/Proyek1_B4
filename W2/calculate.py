def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    mean = total/len(numbers)
    # Calculate the mean of a list of numbers
    return mean
    
def calculate_median(numbers):
    # Calculate the median of a list of numbers
    return
    
def calculate_maximum(numbers):
    # Calculate the maximum of a list of numbers
    return
    
def calculate_minimum(numbers):
    # Calculate the minimum of a list of numbers
    return
    
def calculate_all(numbers):
    # Calculate all statistics (mean, median, maximum, minimum) and return as a dictionary
    results = {
        "Mean": calculate_mean(numbers),
        "Median": calculate_median(numbers),
        "Maximum": calculate_maximum(numbers),
        "Minimum": calculate_minimum(numbers)
    }
    return results