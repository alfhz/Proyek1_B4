def calculate_mean(numbers):
    # Calculate the mean of a list of numbers
    return;
    
def calculate_median(numbers):
    # Calculate the median of a list of numbers
    return;
    
def calculate_maximum(numbers):
    # Calculate the maximum of a list of numbers
    return;
    
def calculate_minimum(numbers):

    if len(numbers) == 0:
        return "List kosong"
    
    nilai_minimum = numbers[0]
    panjang_array = len(numbers)

    for i in range(panjang_array):
       if numbers[i] < nilai_minimum:
           nilai_minimum = numbers[i]

    print("Nilai terkecil adalah: ", nilai_minimum)

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