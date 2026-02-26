from calculate import calculate_mean, calculate_median, calculate_maximum, calculate_minimum, calculate_all
from input_handler import input_numbers, input_choice_menu, input_choice_continue
from display import display_menu, display_all_results, display_result, display_exit_message, display_invalid_option

# Main function to run the Mini Data Analyzer
def main():
    # Loop until user chooses to exit
    while True:
        # Display menu and get user choice
        display_menu()
        choice = input_choice_menu()
        
        # Handle user choice using match-case statement
        match choice:
            case "1":
                numbers = input_numbers()
                mean = calculate_mean(numbers)
                display_result("Mean", mean, numbers)
            case "2":
                numbers = input_numbers()
                median = calculate_median(numbers)
                display_result("Median", median, numbers)
            case "3":
                numbers = input_numbers()
                maximum = calculate_maximum(numbers)
                display_result("Maximum", maximum, numbers)
            case "4":
                numbers = input_numbers()
                minimum = calculate_minimum(numbers)
                display_result("Minimum", minimum, numbers)
            case "5":
                numbers = input_numbers()
                all_in = calculate_all(numbers)
                display_all_results(numbers, all_in)
            case "6":
                display_exit_message()
                break
            case _:
                display_invalid_option()
                
        # Handle if user want to continue        
        choice_continue = input_choice_continue()
        if choice_continue == "n":
            display_exit_message()
            break
                
if __name__ == "__main__":
    main()
