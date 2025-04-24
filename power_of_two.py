#!/usr/bin/env python3

# Author: Tony G

# Date: 2025-04-16

# powers all numbers between 0 and input number to the power of 2.


def main():
    # Get user input
    user_input = input("Enter a non-negative integer: ")

    try:
        # Convert input to integer
        number = int(user_input)

        # Check if the number is non-negative
        if number < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            # Calculate and display squares of numbers from 0 to the input
            for counter in range(number + 1):
                result = counter**2
                print(f"{counter}^2 = {result}")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
