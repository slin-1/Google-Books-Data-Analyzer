# T008_P4_booksUI
# Version 1.0 11/04/22
# Developed by: Steven Lin, Brady Thompson, Nolan Wrigley, and Fisher Walsh

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Import Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------

from load_data import category_dictionary 
from add_remove_search_dataset import *
from sorting_fun import *

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Interface Code
# --------------------------------------------------------------------------------------------------------------------------------------------------

def interface_menu() -> str:
    """
    Outputs the user interface menu, giving the user a list of available commands.
    
    >>> interface_menu()
    
    The available commands are:
       1- L)oad data
       2- A)dd book
       3- R)emove book
       4- G)et books
            T)itle   R)ate   A)uthor   P)ublisher   C)ategory
       5- GCT) Get all Categories for book Title
       6- S)ort books
            T)itle   R)ate   P)ublisher   A)uthor
       7- Q)uit
    """
    
    # Displays the available commands in format
    print("\nThe available commands are:\n   1- L)oad data\n   2- A)dd book\n   3- R)emove book\n   4- G)et books\n        T)itle   R)ate   A)uthor   P)ublisher   C)ategory\n   5- GCT) Get all Categories for book Title\n   6- S)ort books\n        T)itle   R)ate   P)ublisher   A)uthor\n   7- Q)uit")

# --------------------------------------------------------------------------------------------------------------------------------------------------

def add_ui(current_diction: dict) -> dict:
    """
    Presents a user interface for when the user wants to add a book. 
    Returns the new dictionary.
    
    >>> add_ui(current_dictionary)
    
    Please enter a book in the format below
    Title, Author, Language, Publisher, Category, Rating, Pages: Sample Book 1, Steven, English, Steven Inc., New Category, 1.0, 100
    The book has been added correctly
    {[...] 'New Category': [{'title': 'Sample Book 1', 'author': 'Steven', 'language': 'English', 'rating': 1.0, 'publisher': 'Steven Inc.', 'pages': 100}]}
    """
    add_book_counter = 0    # Establishes/resets the add book counter to keep track of attempts
    while add_book_counter < 1:    # Gives the user one attempt to add a book before returning to the available commands
        # User must input the book in a certain format
        input_add = input("Please enter a book in the format below\nTitle, Author, Language, Publisher, Category, Rating, Pages: ")
        input_add = tuple(input_add.replace("N/A", "0.0").split(", "))    # Convert string input to a tuple
        current_diction = add_book(current_diction, input_add)    # Adds the given book using the add_book function
        add_book_counter += 1    # Adds to the user's attempts
    return current_diction

# --------------------------------------------------------------------------------------------------------------------------------------------------

def remove_ui(current_diction: dict) -> dict:
    """
    Presents a user interface for when the user wants to add a book. 
    Returns the new dictionary.
    
    >>> remove_ui(current_dictionary)
    
    Please enter a book title: Antiques Roadkill: A Trash 'n' Treasures Mystery
    Please enter a category: Fiction
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, [...]}
    """
    
    remove_book_counter = 0    # Establishes/resets the remove book counter to keep track of attempts
    while remove_book_counter < 1:    # Gives the user one attempt to remove a book before returning to the available commands
        # User must input the book in a certain format
        input_remove_title = input("Please enter a book title: ")
        input_remove_category = input("Please enter a category: ")
        current_diction = remove_book(current_diction, input_remove_title, input_remove_category)    # Removes the book using the remove_book method
        remove_book_counter += 1    # Adds to the user's attempts        
    return current_diction

# --------------------------------------------------------------------------------------------------------------------------------------------------

def get_books_ui(current_diction: dict) -> None:
    """
    Presents a user interface for when the user wants to obtain a book
    
    >>> get_books_ui(current_dictionary)
    
    How do you want to get books?
	T)itle   R)ate   A)uthor   P)ublisher   C)ategory
    Please type your command: C
    Please enter a category: Investing
    The category Investing has 1 books. This is the list of books:
    Book 1: "The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further" by "Alvin Hall"
    """
    
    subcommandlist = ["T", "R", "A", "P", "C", "Q"] # Incl q to quit to main selection menu
    limit = 3
    y = 0
    while y < limit:
        get_books_input = input("How do you want to get books?\n\tT)itle   R)ate   A)uthor   P)ublisher   C)ategory\nPlease type your command: ").upper()
        if get_books_input not in subcommandlist:
            print("Invalid input. Please try again")
            y += 1
        elif get_books_input == "Q":
            print("Returning to main command selection")
            y = limit
        elif get_books_input == "T":    # Get books by title
            title = input("Enter Title: ")
            get_books_by_title(current_diction, title)
            y = limit
        elif get_books_input == "R":    # Get books by rate
            # This will crash if the user is an idiot, as not allowed to use try except for error handling
            rate = float(input("Enter Rate (as float): "))
            get_books_by_rate(current_diction, rate)
            y = limit
        elif get_books_input == "A":    # Get books by author
            author = input("Enter Author: ")
            get_books_by_author(current_diction, author)
            y = limit
        elif get_books_input == "P":
            publisher_name = input("Please enter a publisher's name: ")    # Asks the user to enter a publishers name
            get_books_by_publisher(current_diction, publisher_name)   # Prints the get_books_by_publisher using the publisher name inputed
            y = limit
        elif get_books_input == "C":
            category_name = input("Please enter a category: ")    # Asks the user to enter a category name
            get_books_by_category(current_diction, category_name)    # Prints the get_books_by_category using the category name inputed
            y = limit
        else:
            print("Command not currently supported\n")
            y += 1    

# --------------------------------------------------------------------------------------------------------------------------------------------------

def get_all_categories_ui(current_diction: dict) -> int:
    """
    Presents a user interface for when the user wants to obtain all the categories of a dictionary
    
    >>> get_all_categories_ui(current_dictionary)
    
    Please enter a book title: Deadpool Kills the Marvel Universe
    The book title Deadpool Kills the Marvel Universe belongs to the following categories:
    Category 1: Comics
    """
    
    book_title = input("Please enter a book title: ") # Prompts the user to enter a book title
    all_categories = get_all_categories_for_book_title(category_dictionary("google_books_dataset.csv"), book_title) # Prints the get_all_categories_for_book_title using the category name inputed    
    return all_categories

# --------------------------------------------------------------------------------------------------------------------------------------------------

def sort_ui(current_diction: dict) -> list:
    """
    Presents a user interface for when the user wants to sort the dictionary into a list
    
    >>> sort_ui(current_diction)
    
    How do you want to sort?
            1- T)itle
            2- R)ate
            3- P)ublisher
            4- A)uthor
            5- Q)uit to main menu

    Please type your command: t
    Books sorted by title:
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'categories': ['Fiction', 'Thrillers']}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'categories': ['Fiction', 'Fantasy', 'Adventure', 'Epic']}, {...}]
    """
    
    choosing_sort = True    # User is choosing a method of sorting
    while choosing_sort:    # Repeats until sorting method is chosen or user quits
        choosing_sort = False    # Choosing sorting method will end unless an invalid command is entered
        print('\nHow do you want to sort?\n\t1- T)itle\n\t2- R)ate\n\t3- P)ublisher\n\t4- A)uthor\n\t5- Q)uit to main menu')    # Print sub UI
        match input('\nPlease type your command: ').upper():    # Displays prompt and takes a command
            case 'T':    # If the user enters T
                print(f'Books sorted by title:\n{sort_books_title(current_diction)}')
            case 'R':    # If the user enters R
                print(f'Books sorted by rating:\n{sort_books_ascending_rate(current_diction)}')
            case 'P':    # If the user enters P
                print(f'Books sorted by publisher:\n{sort_books_publisher(current_diction)}')
            case 'A':    # If the user enters A
                print(f'Books sorted by author:\n{sort_books_author(current_diction)}')
            case 'Q':    # If the user enters Q
                pass    # Do nothing
            case _:    # If the user enters an invalid command
                choosing_sort = True    # User will continue to choose
                print('\n* No such command *')    # Informs the user that the command is not recognized

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Main Script
# --------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    max_attempts = 5    # Used to establish the maximum attempts
    attempts = 0    # Used to keep track of the user's attempts
    choosing = True    # Starts with user choosing command
    file_loaded = False    # Starts with no file loaded
    current_dictionary = {}    # Empty dictionary to hold the current dictionary
    correct_inputs = ["L", "A", "R", "G", "GCT", "S", "Q"]    # List of valid inputs that the user can input (other inputs are considered "invalid")
    supported_files = ['GOOGLE_BOOKS_DATASET.CSV']    # Files that the program will accept
    
    while attempts < max_attempts:
        interface_menu()
        user_input = input("Please type your command: ").upper()    # Prompts for user input, and converts the input to uppercase
        attempts += 1
        
        if user_input not in correct_inputs:    # Invalid input
            print("\nInvalid input")
        elif user_input == "Q":    # Quits the program
            print("Quitting...")
            attempts = max_attempts
        elif user_input == "L":
            choosing_file = True     # User is choosing a file
            while choosing_file:    # Repeats until the user has chosen a file or quit
                file_name = input('Please enter the name of the file you would like to load (Enter "Q" to quit to main menu): ').upper()    # Displays prompt and takes a file name
                if file_name == 'Q':    # If the file name is Q
                    choosing_file = False    # Exits to the main menu
                elif file_name in supported_files:    # If the file is supported
                    current_dictionary = category_dictionary(file_name)    # Creates a dictionary of books using the file
                    file_loaded = True    # A file has been loaded successfully
                    choosing_file = False    # File is no longer being chosen
                    print(f'Loaded {file_name}')    # Informs the user that the file has been loaded
                else:
                    print(f'\n* The file {file_name} is not supported *\n')    # Informs the user that the file is not supported
        elif file_loaded == False:    # Checks if the user has successfully loaded a file 
            print("File not loaded")
        elif user_input == "A" and file_loaded:    # If the user inputs "A" and a file is loaded
            current_dictionary = add_ui(current_dictionary)
            print(current_dictionary)
        elif user_input == "R" and file_loaded:    # If the user inputs "R" and a file is loaded
            current_dictionary = remove_ui(current_dictionary)
            print(current_dictionary)
        elif user_input == "G" and file_loaded:    # If the user inputs "G" and a file is loaded
            get_books_ui(current_dictionary)
        elif user_input == "GCT" and file_loaded:    # If the user inputs "GCT" and a file is loaded
            get_all_categories_ui(current_dictionary)
        elif user_input == "S" and file_loaded:    # If the user inputs "S" and a file is loaded
            sort_ui(current_dictionary)

print("Program has quit")    # Indicates that the program has stopped