def calculate_mean(numbers):
    # Calculate the mean of a list of numbers
    return;
    
def calculate_median(numbers):
    # Calculate the median of a list of numbers
    return;
    
def calculate_maximum(numbers):
    nilai_maksimum = numbers[0]
    for num in numbers:
        if num > nilai_maksimum:
            nilai_maksimum = num
    return nilai_maksimum
    
def calculate_minimum(numbers):
    # Calculate the minimum of a list of numbers
    return;
    
def calculate_all(numbers):
    # Calculate all statistics (mean, median, maximum, minimum) and return as a dictionary
    results = {
        "Mean": calculate_mean(numbers),
        "Median": calculate_median(numbers),
        "Maximum": calculate_maximum(numbers),
        "Minimum": calculate_minimum(numbers)
    }
    return results