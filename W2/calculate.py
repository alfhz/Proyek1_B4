import statistics

def calculate_mean(numbers):
    # Calculate the mean of a list of numbers
    total = 0
    for num in numbers:
        total += num
    mean = total/len(numbers)
    return mean
    
def calculate_median(numbers):
    # Calculate the median of a list of numbers
    if not numbers:
        return None
    return statistics.median(numbers)
    
def calculate_maximum(numbers):
    # Search the biggest number of a list of number
    nilai_maksimum = numbers[0]
    for num in numbers:
        if num > nilai_maksimum:
            nilai_maksimum = num
    return nilai_maksimum
    
def calculate_minimum(numbers):
    # Search the smallest number of a list of number

    if len(numbers) == 0:
        return "List kosong"
    
    nilai_minimum = numbers[0]
    panjang_array = len(numbers)

    for i in range(panjang_array):
        if numbers[i] < nilai_minimum:
            nilai_minimum = numbers[i]

    return nilai_minimum
    
def calculate_all(numbers):
    # Calculate all statistics (mean, median, maximum, minimum) and return as a dictionary
    results = {
        "Mean": calculate_mean(numbers),
        "Median": calculate_median(numbers),
        "Maximum": calculate_maximum(numbers),
        "Minimum": calculate_minimum(numbers)
    }
    return results