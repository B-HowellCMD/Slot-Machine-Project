import random

MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum amount to bet on each line
MIN_BET = 1   # Minimum amount to bet on each line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):  # Function to get the slot machine
    all_symbols = []  # List to store all the symbols
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]  # List to store the columns
    for col in range(cols):
        column = []  # List to store the symbols in the column
        for row in range(rows):
            value = random.choice(all_symbols)  # Get a random symbol


def deposit():  # Function to get the amount to deposit
    while True:
        # Get the amount to deposit
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():  # Check if the amount is a number
            amount = int(amount)    # Convert the amount to an integer
            if amount > 0:  # Check if the amount is greater than 0
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")

    return amount


def get_number_of_lines():  # Function to get the number of lines to bet on
    while True:
        # Get the number of lines to bet on
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # Check if the number of lines is between 1 and MAX_LINES
                break
            else:
                print(f"Lines must be between 1 and {MAX_LINES}")
        else:
            print("Amount must be a number")

    return lines


def get_bet():  # Function to get the amount to bet on each line
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # Check if the amount is between MIN_BET and MAX_BET
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Amount must be a number")

    return amount


def main():  # Main function
    balance = deposit()
    lines = get_number_of_lines()
    while True:  # Loop until the bet is valid
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:  # Check if the bet is greater than the balance
            print(
                f"You do not have enough money to make that bet. Your current balance is ${balance}.")  # Print the balance
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")  # Print the bet


main()  # Call main function
