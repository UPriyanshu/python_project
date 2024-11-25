# 590016430 PRIYANSHU UNIYAL (MCA)

## Modern GUI Calculator

A sleek and user-friendly calculator application built with Python and Tkinter. This calculator features a modern design with color-coded buttons and smooth operation for basic arithmetic calculations.

## Description

This calculator application provides a graphical user interface for performing basic mathematical operations. It features:
- Clean and intuitive interface
- Color-coded buttons for better user experience
- Error handling for invalid calculations
- Support for basic arithmetic operations (+, -, *, /)

## Screenshots

![image](https://github.com/user-attachments/assets/d2c0c5c0-436f-4615-8fef-1c951b3c5e7a)


![image](https://github.com/user-attachments/assets/e28470d5-f7fe-4daa-b9ba-c0f154325334)

![image](https://github.com/user-attachments/assets/dc854cff-8772-4f14-ad0b-b70b6fa1b6b1)

![image](https://github.com/user-attachments/assets/78be7316-3e0d-4c0e-be5d-4e91e672a467)

![image](https://github.com/user-attachments/assets/50f1622f-f56c-4a9e-90f1-06455310f19e)

![image](https://github.com/user-attachments/assets/264e2b96-0938-4b1c-b40c-194be689682e)


## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Function Descriptions

### Class: CalculatorApp

#### `__init__(self, root)`
- Initializes the calculator window
- Sets up the display and creates the button grid
- Configures the initial styling and layout

#### `button_click(self, value)`
- Handles all button click events
- Parameters:
  -  The value of the button clicked (number, operator, or command)
- Functionality:
  - Processes numeric inputs
  - Handles arithmetic operations
  - Performs calculations when '=' is pressed
  - Clears display when 'C' is pressed
  - Includes error handling for invalid calculations

## Features

1. **Display Window**
   - Large, easy-to-read display
   - Right-aligned text for better readability

2. **Operation Buttons**
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)

3. **Special Buttons**
   - Clear (C): Resets the calculator
   - Equals (=): Computes the result

4. **Color Coding**
   - Numbers: Light gray
   - Operators: Light blue
   - Clear: Light red
   - Equals: Light green

