# Pickling and Structured Error Handling

## Introduction
The goal of this assignment was to write a program that demonstrates the use of pickling methods and exception handling. A ***Menu*** class is used to display to the user the various examples in the application and gets input from the user for their choice.
1)	[Pickling] Append binary data to a file.
2)	[Pickling] Read and display data from binary file.
3)	[Error Handling] Basic try / except example.
4)	[Error Handling] Using try / except to capture and print the exception.
5)	[Error Handling] Using try / except to look for a specified exception.
6)	[Error Handling] Using raise to cause a custom exception.
7)	Exit program.

The two remaining classes, Pickling and ErrorHandling, contain the code to the various methods described in the menu.

## The Pickling Class
**AppendBinaryData() Function**

This function gets data in the form of an ***Item ID*** and ***Item Name*** from the user, then opens a file in append binary mode, then writes the data to the file using the ***pickle.dump()*** function.  (Figures 1 & 2)

![Figure 1. Using pickle.dump() to write data to a binary file.](./image1.png)
