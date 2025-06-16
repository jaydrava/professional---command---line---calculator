from app.calculation.calculation import CalculationFactory

calculation_history = []

def show_help():
    """ Displays the help message for the calculator. """
    print("\nAvailable commands:")
    print(" +, -, *, / : Perform arithmetic operations")
    print(" history : Show calculation history")    
    print("help : Show this help menu")
    print("exit : Exit the calculator")

def run_calculator():
    print("Welcome to the Command Line Calculator!")
    show_help()

    while True:
        user_input = input(
            "\nEnter operator (+, -, *, /) or command (help, history, exit):").strip()
        
        if user_input.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == "help":
            show_help()
            continue
        elif user_input.lower() == "history":
            if not calculation_history:
                print("No calculations performed yet.")
            else:
                print("\nHistory of calculations:")
                for i, calc in enumerate(calculation_history, start=1):
                    print(f"{i}: {calc.a} {calc.operator.__name__} {calc.b} = {calc.result}")
            print()  # Print a newline for better readability
        elif user_input in ["+", "-", "*", "/"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                #Handle division by zero early
                if user_input == "/" and b == 0:
                    print("Error: Division by zero is not allowed.\n")
                    continue # pragma: no cover

                #Create and store the calculation
                calc = CalculationFactory.create_calculation(a, b, user_input)
                calculation_history.append(calc)
                print(f"Result: {calc.get_result()}\n")

            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
            except Exception as e:
                print(f"An error occurred: {e}\n")
        else:
            print("Invalid command. Type 'help' for a list of commands.\n") # pragma: no cover