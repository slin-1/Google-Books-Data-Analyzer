# Google-Books-Data-Set
Version 1.0 12/04/22

## Description
This software allows the manipulation and extraction of information
from a set of data. It allows the user to select a file from which to
import data and then allows them a wide range of options to manipulate
that data.

Project is composed of these files:

`google_books_dataset.csv`  
_sample dataset to buid library from_  
`T008_check_equal.py`  
_simple unit testing function_  
`T008_P2_add_remove_search_dataset.py`  
_contains functions to add, remove and search the dataset_  
`T008_P3_sorting_fun.py`  
_contains functions to sort the dataset_  
`T008_P4_booksUI.py`  
_the user interface for this program_  
`T008_P5_load_data.py`  
_the function that converts dataset to dictionary_

## Installation
Python version 3.10 or later
No external python libraries are used.

## Usage
Launch the main script program for user interface `T008_P4_booksUI.py`
follow instructions to select data file to load.

To begin, enter the command "L" to be able to select file to load.

\>>> Please type your command: l  
\>>> Enter name of file to load: example.csv  
\>>> Loaded EXAMPLE.CSV

You should then be prompted to select a command

\>>> Please type your command: 

After selecting command, you will either be prompted for command-specific
information or be prompted to select a specific variation of command.

\>>> How do you want to proceed?  
\>>> Please type your command: 

(you will now be prompted for command-specific information)

**OR**

\>>> Enter subsequent query: 

The program will now either fetch information from the database or allow the
user to manipulate the database.

## Credits
Functions created by:

**Steven Lin**

`book_category_dictionary`  
_creates a dictionary from the dataset, grouped by category._  
`add_book`  
_allows the user to add a book to the dictionary._  
`remove_book`  
_allows the user to remove a book from the dictionary._  
`sort_books_title`  
_sorts the books by title and groups categories._  
_created user interface for add and remove book._  

**Brady Thompson**

`book_publisher_dictionary`  
_creates a dictionary from the dataset, grouped by publisher. (not in final)_  
`get_books_by_category`  
_lets the user query what books are in a specific category._  
`get_books_by_rate`  
_lets the user query which books are at a specific rate._  
`sort_books_publisher`  
_sorts the books by publisher (title if same) and groups categories._  
_created user interface for get books by title, rate, and author._  

**Nolan Wrigley**

`book_author_dictionary`  
_creates a dictionary from the dataset, grouped by author. (not in final)_  
`get_books_by_title`  
_lets the user search for a book by title._  
`get_books_by_author`  
_a search function to search for all books by a specific author._  
`sort_books_author`  
_sorts the books by author (title if same) and groups categories._  
_created user interface for get books by publisher and category and
get all categories for book title._  

**Fisher Walsh**

`book_list`  
_creates a dictionary from the dataset, of each book. (not in final)_  
`get_books_by_publisher`  
_search function for specific publishers._  
`get_all_categories_for_book_title`  
_returns all categories for a specific book._  
`sort_books_ascending_rate`  
_sorts the books by rate (title if same), rating of 'N/A' first.
also groups categories._  
_created user interface for sort books and subcommands._  

## License
<!--This software is simple and therefore licensed as broadly as possible.-->

Copyright (C) 2022 Steven Lin <stevenlin3@cmail.carleton.ca> et al.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE
USE OR PERFORMANCE OF THIS SOFTWARE.
