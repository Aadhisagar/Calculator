# Calculator Application using Python Tkinter

## Project Overview

This project is a simple graphical calculator developed using Python's Tkinter library. It provides basic arithmetic operations such as addition, subtraction, multiplication, division, and percentage calculations through an interactive user interface.

## Features

* User-friendly graphical interface
* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Percentage (%)
* Decimal number support
* Clear (C) and Clear Entry (CE) functions
* Result display with four decimal places

## Technologies Used

* Python 3.x
* Tkinter (GUI Library)

## Project Structure

* Main Window Creation
* Display Screen
* Number Buttons (0-9)
* Arithmetic Operator Buttons
* Event Handling Functions
* Calculation Logic

## Functions Description

### update_value()

Updates the calculator display with formatted output.

### number_click_event()

Handles number button clicks and updates the current input.

### format_number()

Combines integer and decimal parts into a complete number.

### Event_click()

Acts as the central event handler for all button actions.

### operator_click_event()

Stores the selected arithmetic operator and first operand.

### clear_click()

Clears the current input values and resets decimal status.

### calculate_result()

Performs the arithmetic operation and displays the result.

### std_btn()

Creates calculator buttons dynamically.

## How to Run

### Step 1: Install Python

Download and install Python from:
https://www.python.org

### Step 2: Save the Program

Save the source code as:

calculator.py

### Step 3: Run the Program

Open Command Prompt or Terminal and execute:

python calculator.py

## Sample Operations

| Input   | Operation      | Output |
| ------- | -------------- | ------ |
| 10 + 20 | Addition       | 30     |
| 50 - 15 | Subtraction    | 35     |
| 8 * 5   | Multiplication | 40     |
| 100 / 4 | Division       | 25     |
| 50 %    | Percentage     | 0.5    |

## Error Handling

* Division by zero is handled using exception handling.
* Invalid operations are prevented through input validation.

## Future Enhancements

* Square root operation
* Scientific calculator functions
* Keyboard input support
* Calculation history
* Dark mode theme

