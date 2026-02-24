from display import display_invalid_option

def input_choice_menu():
    # Input user choice menu
    choice = input("Enter your choice (1-6): ")
    return choice

def input_numbers():
    # Input list of numbers from user
    input_str = input("Enter a list of numbers (11,20,1,3,...): ")
    # Split inputan base on comma and convert to list of integers
    numbers = [int(num.strip()) for num in input_str.split(",")]
    return numbers

def input_choice_continue():
    # Input user choice continue or exit
    while True:
        choice_continue = input("Do you want to continue? (y/n): ").lower()
        
        if choice_continue in ["y", "n"]:
            return choice_continue
        else:
            display_invalid_option()
