```markdown
# Simple Calculator

This is a simple command-line calculator program written in Python. It provides basic arithmetic operations, square root, exponentiation, and history tracking.

## Features

-   **Addition:** Adds two numbers.
-   **Subtraction:** Subtracts the second number from the first.
-   **Multiplication:** Multiplies two numbers.
-   **Division:** Divides the first number by the second. Handles division by zero errors.
-   **Modulus (Remainder):** Returns the remainder of the division.
-   **Square Root:** Calculates the square root of a number. Handles negative input errors.
-   **Exponentiation:** Raises the first number to the power of the second.
-   **History:** Stores and displays a history of calculations.
-   **Clear History:** Clears the calculation history.
-   **Input Validation:** Validates user input for menu choices.

## How to Use

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2.  **Navigate to the directory:**

    ```bash
    cd <repository_directory>
    ```

3.  **Run the Python script:**

    ```bash
    python calculator.py
    ```

4.  **Follow the on-screen prompts:**

    -   Enter the number corresponding to the desired operation.
    -   Enter the required numbers for the calculation.
    -   View or clear the calculation history as needed.
    -   Enter '10' to exit the calculator.

## Example

```
welcome to simple calculator
Entre your choice from below
1. add
2. subtract
3. multiply
4. divide
5. remainder/modulas
6. Square Root
7. exponentiation
8.view history
9.clear history
10. EXIT
Enter your choice:1
Enter first number5
Enter second number3
The addition is:8.0

welcome to simple calculator
Entre your choice from below
1. add
2. subtract
3. multiply
4. divide
5. remainder/modulas
6. Square Root
7. exponentiation
8.view history
9.clear history
10. EXIT
Enter your choice:8

:---Calculation of history---
(1, '5.0+3.0=8.0')

welcome to simple calculator
Entre your choice from below
1. add
2. subtract
3. multiply
4. divide
5. remainder/modulas
6. Square Root
7. exponentiation
8.view history
9.clear history
10. EXIT
Enter your choice:10
THANK YOU
THANKS
```

## Code Structure

-   `choices()`: Displays the menu of available operations.
-   `get_choice()`: Gets and validates user input for the menu choice.
-   `add(x, y)`: Adds two numbers.
-   `sub(x, y)`: Subtracts two numbers.
-   `mul(x, y)`: Multiplies two numbers.
-   `div(x, y)`: Divides two numbers.
-   `mod(x, y)`: Calculates the modulus of two numbers.
-   `sqrt(x)`: Calculates the square root of a number.
-   `expo(x,y)`: calculates the exponent of a number.
-   `view_history()`: Displays the calculation history.
-   `clear_history()`: Clears the calculation history.
-   The main `while` loop: Controls the program flow, gets user input, performs calculations, and manages history.

## Requirements

-   Python 3.x

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes or feature requests.

## License

This project is licensed under the MIT License.
```
