# Task1
This is a simple Python program that:

  Accepts a user-defined number of elements,

  Stores them in a list (array),

  Displays the array before and after sorting.

# Task2a
This is a simple python program that demonstrates:

 - How to redirect printed output to a file using the `file=` parameter in `print()`.
 - How to force immediate writing to the file using the `flush=True` parameter.
 - Use of `flush` to control buffering behavior in console output.

# Task2b

This repository contain a python script that demonstrates the functionality of various types of operators in Python, including:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Special Operators

# Task3a

This simple Python program allows users to **view the calendar of any month and year** they input.
It uses Python's built-in `calendar` module to display a neatly formatted calendar in the terminal.
## Features

- Asks user for a **year** and **month (1-12)**
- Validates the input to ensure the month is within a valid range
- Displays the monthly calendar for the given inputs

# Task3b

This Python program allows users to view the **calendar for any given month and year**, using only the built-in `datetime` module — without relying on the `calendar` module.

## Features

- Prompts the user to input a year and a month (1–12)
- Calculates and prints the calendar layout for the specified month
- Handles month transitions and proper weekday alignment
- No third-party libraries required — built using only the standard `datetime` module

# task4
 This Python script demonstrates basic bitwise operations such as XOR, left shift, and right shift.
 ## Description
 The program performs the following:

  1. Initializes two integers x and y.

  2. Displays their values.

  3. Calculates and prints:

     - Bitwise XOR of x and y

     - Left shift of x by 2 positions

     - Right shift of x by 2 positions

# task5
  This is a console-based ATM simulation program written in Python. It demonstrates various control flow constructs such as:

    -if, elif, else

    -for loop

    -while loop

    -break, continue

    -exit() function

 The application simulates an ATM machine's functionality and allows the user to:

    -Authenticate using a 4-digit ATM PIN

    -Check their account balance

    -Withdraw and deposit money

    -Change their ATM PIN

    -Exit the system

# task6a

This Python program demonstrates various list operations such as:

  -Adding, inserting, extending, and removing elements

  -Counting and finding index

  -Sorting and reversing the list

  -Slicing and copying

  -Using functions like sum(), min(), and max()

# task6b

This Python program demonstrates various operations on tuples, including:

  -Tuple creation

  -Basic functions like len(), max(), min(), and sum()

  -Tuple slicing, repetition, and membership testing

  -Conversion from list to tuple

  -Counting and indexing values

  -Tuple unpacking

# task6c
## Python Dictionary Operations - Student Record Example

  This Python program demonstrates various operations on a dictionary using a sample `student` record. It includes creation, access, update, deletion, copying, and other useful dictionary methods in Python.

# task6d
## Python Set Operations - Demo Program

  This Python script demonstrates common operations on sets using a sample set of integers. It showcases how to add, remove, and manipulate sets using built-in Python methods.

# task7a
  This Python program demonstrates how to sort a **list of tuples** based on the **second item** (typically a numeric value like marks or scores) using a **lambda function** as the sorting key.

# task7b
  ##  Python Simple Calculator using Functions and Loop

  This Python program implements a basic calculator that can perform arithmetic operations like addition, subtraction, multiplication, division, and modulus using user-defined functions and a loop.

# task8
  ## Money & Item Operations in Python

  This Python program demonstrates **real-life object-oriented programming (OOP)** concepts by modeling money transactions and item purchases using **operator overloading**.

  ##  Description

  The project contains two main classes:

  ### 1. `Money` Class
  Represents a person's money or wallet balance.

  #### Features:
  - `+` Add two money amounts
  - `-` Subtract one amount from another
  - `*` Multiply a money amount by a number (e.g., double the money)
  - Custom string representation using `__str__`

  ### 2. `Item` Class
  Represents a purchasable item with a fixed price.

  #### Features:
  - `*` Multiply the price of the item with a quantity to return the total cost (as a `Money` object)
  - Custom string representation using `__str__`
# task9
  ## Fruit Count Visualization Using Matplotlib
    This Python project uses `matplotlib` to visually represent the count of different fruits using three types of charts:
      - Line Plot
      - Pie Chart
      - Bar Chart
# task10
  ## Streamlit Plots Using Matplotlib
    This Streamlit web app demonstrates how to create a **2x2 subplot layout** using Matplotlib to visualize insights from the `tip.csv` dataset.

  The app includes:
    - Histogram of total bills
    - Boxplot of tips
    - Pie chart of gender distribution
    - Bar chart of average total bill by day

# task11
  ### This Python script performs a series of text preprocessing tasks on raw input data. It uses the `re` (regular expressions) module to identify and clean specific patterns in the text, such as dates, email addresses, excessive spaces, emojis, and more.
#### 📌 Features

The script performs the following cleaning operations **in sequence**:

1. **Extract and remove numeric dates**  
   Matches and removes dates in the format:  
   - `dd/mm/yyyy`  
   - `yyyy-mm-dd`  
   - `dd-mm-yyyy`

2. **Remove textual (written) date formats**  
   Example:  
   - `July 4, 2025`  
   - `Dec 25, 2024`  
   Supports both full and short month names.

3. **Remove email addresses**  
   Specifically targets emails ending in `.com`.

4. **Remove emojis and non-ASCII characters**  
   Removes any Unicode characters outside the standard ASCII range.

5. **Simplify excessive punctuation**  
   Converts repeated punctuation (e.g., `!!!` or `...`) into a single character (e.g., `!`, `.`).

6. **Normalize whitespace**  
   Replaces multiple spaces or newlines with a single space.

# task12
   This Python program demonstrates basic **Natural Language Processing (NLP)** tasks using the **spaCy** library. It covers key components such as tokenization, custom token rules, part-of-speech tagging, stopword filtering, and lemmatization.
