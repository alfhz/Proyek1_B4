# Display module for Mini Data Analyzer

def display_menu():
    print("=== Mini Data Analyzer ===")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Maximum")
    print("4. Calculate Minimum")
    print("5. Calculate All")
    print("6. Exit")
    print("============================")

def display_all_results(numbers, results):
    print("Input Numbers:", numbers)
    #
    for key, value in results.items():
        print(f"{key}: {value}")
        
def display_result(operation, result, numbers):
    print(f"Input Numbers: {numbers}")
    print(f"{operation}: {result}")
    
def display_exit_message():
    print("Thank you for using Mini Data Analyzer. Goodbye!")
    
def display_invalid_option():
    print("Invalid option. Please choose a valid menu option.")
