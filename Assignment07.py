# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstration of Pickling and Structured Error Handling using
#              a main menu that calls the various demonstration functions.
# ChangeLog (Who,When,What):
# Richard Sauer,5/28/2023,Created Script
# ---------------------------------------------------------------------------- #
import pickle  # Needed for binary file operations

class Menu:
    """ Performs menu tasks """
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user.
        :return: nothing
        """
        print('''
            Menu of Options
            1) [Pickling] Append binary data to a file.
            2) [Pickling] Read and display data from binary file.
            3) [Error Handling] Basic try / except example.
            4) [Error Handling] Using try / except to capture and print the exception.
            5) [Error Handling] Using try / except to look for a specified exception.
            6) [Error Handling] Using raise to cause a custom exception.        
            7) Exit program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user.
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for better formatting
        return choice

class Pickling:
    """ Performs Pickling tasks """
    @staticmethod
    def AppendBinaryData():
        """ Gets data from the user writes it to a binary file.
        :return: nothing
        """
        itemId = str(input("Enter item ID: "))
        itemName = str(input("Enter item name: "))
        lstItemData = [itemId, itemName]
        objFile = open("ItemDatabase.dat", "ab")
        pickle.dump(lstItemData, objFile)
        print("Data: " + str(lstItemData) + " saved to file.")
        objFile.close()

    @staticmethod
    def ReadBinaryData():
        """ Shows the current items in the database using try/except to find end of file.
        :return: nothing
        """
        try:
            objFile = open("ItemDatabase.dat", "rb")
        except Exception as e:
            print(e)
            print("Try option 1 to write data to file first.")
        else:
            seperatorText = "----------"
            print("******* Contents of Database *******")
            print("{:10} {:20}".format("Item ID", "Item Name"))
            print("{:10} {:20}".format(seperatorText, seperatorText))
            while True:
                try:
                    lstItemData = pickle.load(objFile)
                    print("{:10} {:20}".format(lstItemData[0], lstItemData[1]))
                except EOFError:
                    break
            objFile.close()

class ErrorHandling:
    """ Performs Error Handling example tasks """
    @staticmethod
    def BasicTryExcept():
        """ Shows use of try / except.
        :return: nothing
        """
        try:
            print("30 / 0", end=" = ")
            print(str(30 / 0))
            # myValue = 30 / 0
        except:
            print("Custom message: An exception occurred.")
        finally:
            print("30 * 0", end=" = ")
            print(str(30 * 0))

    @staticmethod
    def TryExceptCapture():
        """ Captures exception and shows details.
        :return: nothing
        """
        try:
            print("30 / 0", end=" = ")
            print(str(30 / 0))
        except Exception as e:
            print(e)
            print(type(e))
            print(e.__doc__)

    @staticmethod
    def TrySpecifiedException():
        """ Looks for specific exception.
        :return: nothing
        """
        try:
            print("30 / 0", end=" = ")
            print(str(30 / 0))
        except ZeroDivisionError:
            print("Custom message: Division by zero exception occurred.")
        except Exception as e:
            print(e)

    @staticmethod
    def RaiseExample():
        """ Shows use of raising a custom exception.
        :return: nothing
        """
        try:
            print("x = -21")
            x = -21
            if (x < 0):
                raise Exception("Custom message: Sorry, a negative number was not expected.")
        except Exception as e:
            print(e)

# Main Body of Script  ------------------------------------------------------ #


# Display a menu of choices to the user and call the appropriate function
while (True):
    Menu.output_menu_tasks()  # Shows menu
    choice_str = Menu.input_menu_choice()  # Get menu option

    # Process user's menu choice
    if choice_str.strip() == '1':  # [Pickling] Append binary data to a file.
        Pickling.AppendBinaryData()
        continue  # to show the menu

    elif choice_str == '2':  # [Pickling] Read and display data from binary file.
        Pickling.ReadBinaryData()
        continue  # to show the menu

    elif choice_str == '3':  # [Error Handling] Basic try / except example.
        ErrorHandling.BasicTryExcept()
        continue  # to show the menu

    elif choice_str == '4':  # [Error Handling] Using try / except to capture and print the exception.
        ErrorHandling.TryExceptCapture()
        continue  # to show the menu

    elif choice_str == '5':  # [Error Handling] Using try / except to look for a specified exception.
        ErrorHandling.TrySpecifiedException()
        continue  # to show the menu

    elif choice_str == '6':  # [Error Handling] Using raise to cause a custom exception.
        ErrorHandling.RaiseExample()
        continue  # to show the menu

    elif choice_str == '7':  # Exit Program
        print("Thanks for running the Pickling and Error Handling application!")
        break  # and Exit the program
# end of Main Body
