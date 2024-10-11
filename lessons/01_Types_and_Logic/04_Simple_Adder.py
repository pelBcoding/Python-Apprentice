"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
from tkinter import messagebox, simpledialog, Tk
# Import the required modules
window = Tk()     # Create a window object
window.withdraw()
# Create a window object
number1 = simpledialog.askfloat("", "Please enter in the first number.")
# Hide the window, hint: use the withdraw method
number2 = simpledialog.askfloat("", "Please enter in the second number.")
# Ask the user for the first number   
#number1 = "number1"
#number2 = "number2"
messagebox.showinfo("number1 + number2", str(number1 + number2))
# Ask the user for the second number

# Display the sum of the two numbers 

# Keep the window open
window.mainloop()
