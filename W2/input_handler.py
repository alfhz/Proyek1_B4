def input_choice():
    # Input user choice menu
    choice = input("Enter your choice (1-6): ")
    return choice

def input_numbers():
    # Input list of numbers from user
    input_str = input("Enter a list of numbers (11,20,1,3,...): ")
    # Split inputan base on comma and convert to list of integers
    numbers = [int(num.strip()) for num in input_str.split(",")]
    return numbers