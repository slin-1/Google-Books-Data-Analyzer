# T008_P3_sorting_fun
# Version 1.0 11/04/22
# Developed by: Steven Lin, Brady Thompson, Nolan Wrigley, and Fisher Walsh

# Imports
from check_equal import check_equal

# --------------------------------------------------------------------------------------------------------------------------------------------------
# The four functions from P3 - Task 1 (and additional refactoring function(s))

# Converts a dictionary to a list
def books_to_list(book_dict: dict) -> list:
    """
    Accepts a dictionary of books, sorted according to category, and returns the
    books as dictionaries contained in a list, with the new attribute
    'categories' added to them, which contains any category they were part of in
    the original dictionary.

    >>> books_to_list({'Fiction': [{'title': 'book_1', 'author': 'author_1'}, {'title': 'book_2', 'author': 'author_2'}], 'Fantasy': [{'title': 'book_1', 'author': 'author_1'}]})
    [{'title': 'book_1', 'author': 'author_1', 'categories': ['Fiction', 'Fantasy']}, {'title': 'book_2', 'author': 'author_2', 'category': 'Fantasy'}]
    """
    book_list = []    # Creates empty list of books
    for category, books in book_dict.items():    # For each category amd book in the items of book_dict
        for book in books:    # For each book in the list of books
            searching = True    # Searching for a book
            book_index = 0    # Index of the current book
            while (book_index < len(book_list)) and searching:    # While the index of the current book is less than the length of the list of books, and while the book is still being searched for
                if book.get('title') == book_list[book_index].get('title'):    # If the title of the book matches a title already in the list of books
                    existing_categories = book_list[book_index].get('category')    # Get the categories of the existing book
                    if isinstance(existing_categories, list):    # If the categories are stored as a list
                        if category not in existing_categories:    # If the category does not already exist
                            book_list[book_index]['category'] += [category]    # Add the cateogry to the book's list of categories
                    else:    # If the categories are not stored as a list
                        if category != existing_categories:    #If the category does not already exist
                            book_list[book_index]['category'] = [existing_categories] + [category]    # Create a list with the previous and new category
                    searching = False    # Stop searching for the book
                book_index += 1    # Move to the next index of the list
            if searching:    # If the above loop completes without the book being found
                book_list += [book]    # Add the book to the list of books
                book_list[book_list.index(book)]['category'] = category    # Add the current category to the book
    return book_list    # Return the list of books


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Steven Lin
# P3 - sort_books_title

def sort_books_title(dictionary: dict) -> list:
    """
    Returns a list sorted by their titles based on alphabetical order 
    given a dictionary with keys and respective values.
    
    >>> sort_books_title(category_dictionary("google_books_dataset.csv"))
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'category': ['Fiction', 'Thrillers'], 'pages': 300}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic'], 'pages': 864}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic'], 'pages': 4544}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.7, 'publisher': 'Blake Pierce', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': 250}, ...]
    """
    
    # Converts the dictionary into a list, and combines duplicate books that have different categories
    book_list = books_to_list(dictionary)
    
    # Sorts the list - Bubble Sort Algorithm
    n = len(book_list)
    for c in range(n):    # Iterates thorugh the list elements
        for d in range(n-c-1):
            # Swap if the element found is greater than the next element
            # Sorts alphabetically by the title
            if book_list[d].get("title") > book_list[d+1].get("title"):
                book_list[d], book_list[d+1] = book_list[d+1], book_list[d]
            
    return book_list   # Returns the new and alphabetically ordered book list


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Brady Thompson
# P3 - sort_books_publisher

def sort_books_publisher(dictionary: dict) -> list:
    """Returns aplhabetized list of publishers.
    Of the same publishers, sort alphabetically by title
    When there are 2 books in a row with the same title, create list
    of categories that book is in
    
    #alphabetize by publisher
    >>> sort_books_publisher({'economics':[{'title': 'rich dad poor dad', 'publisher': 'indigo'}, {'title': 'the gamestop short squeeze', 'publisher': 'amazon'}]})
    [{'title': 'the gamestop short squeeze', 'publisher': 'amazon', 'category': 'economics'}, {'title': 'rich dad poor dad', 'publisher': 'indigo', 'category': 'economics'}]
    #alphabetize by title if same publisher
    >>> sort_books_publisher({'music':[{'title': 'zz-top a history', 'publisher': 'universal records'}, {'title': 'all about pink floyd', 'publisher': 'universal records'}]})
    [{'title': 'all about pink floyd', 'publisher': 'universal records', 'category': 'music'}, {'title': 'zz-top a history', 'publisher': 'universal records', 'category': 'music'}]
    #create category sublists in output if same title
    >>> sort_books_publisher({'self-improvement':[{'title': 'atomic habits', 'publisher': 'books&stuff'}], 'buisness'[{'title': 'atomic habits', 'publisher': 'books&stuff'}]})
    [{'title': 'atomic habits', 'publisher': 'books&stuff', 'category': ['self-improvement', 'buisness']}]
    #dictionary with 1 element
    >>> sort_books_publisher({'instructional':[{'title': 'reading books for dummies', 'publisher': 'wiley'}]})
    [{'title': 'reading books for dummies', 'publisher': 'wiley', 'category': 'instructional'}]
    #2 identical books
    >>> sort_books_publisher({'mental health':[{'title': 'being unique', 'publisher': 'canada mental health association'}, {'title': 'being unique', 'publisher': 'canada mental health association'}]})
    [{'title': 'being unique', 'publisher': 'canada mental health association', 'category': 'mental health'}]
    """
    
    # Converts the dictionary into a list, and combines duplicate books that have different categories
    book_list = books_to_list(dictionary)

    #bubble sort the list
    n = len(book_list)
    for x in range(n):
        for y in range(0, n-x-1):
            #sort by publisher
            if book_list[y].get("publisher") > book_list[y+1].get("publisher"):
                book_list[y], book_list[y+1] = book_list[y+1], book_list[y]
            #sort by title if same publisher
            elif book_list[y].get("publisher") == book_list[y+1].get("publisher") and book_list[y].get("title") > book_list[y+1].get("title"):
                book_list[y], book_list[y+1] = book_list[y+1], book_list[y]
    
    return book_list


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Nolan Wrigley
# P3 - sort_books_author

def sort_books_author(dictionary: dict):
    """
    Takes in a given dictionary of different categories as keys and values of dictions including book title, author, rating, etc.
    Sorts the given dictionary into a list organized alphabetically by author. If the name of an author is repeated, the book titles are organized alphabetically.
    
    >>> sort_books_author(category_dictionary("google_books_dataset.csv"))
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'language': 'English', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'category': ['Humor'], 'pages': 112}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Detective', 'Thrillers', 'Mystery'], 'pages': 224}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Detective', 'Thrillers', 'Classics', 'Horror'], 'pages': 208}, {...}]
    """
    
    book_list = books_to_list(dictionary)
    
    # Sorts the list into alphabetical by author using bubble sort
    for o in range(len(book_list)):
        for p in range(len(book_list) - o):
            placeholder1 = book_list[p]
            
            # Checks if the author in the last position is not the same as the current one in the index.
            if book_list[p].get("author") != book_list[-1].get("author"):
                placeholder2 = book_list[p + 1]
                
                # If the current books author name is greater alhpabetically than the book following it, it swaps the two placeholder entries
                if book_list[p].get("author") > book_list[p + 1].get("author"):
                    book_list[p] = placeholder2
                    book_list[p + 1] = placeholder1
    
    # If an authors name appears more than once, organizes their book titles alphabetically using bubble sort
    for q in range(len(book_list)):
        for r in range(len(book_list) - (q+1)):
            placeholder1 = book_list[r]
            
            # If the indexs author is the same as the indexs author following it, creates a second placeholder
            if book_list[r].get("author") == book_list[r + 1].get("author"):
                placeholder2 = book_list[r + 1]
                
                # If the current books title is greater alhpabetically than the book following it, it swaps the two placeholder entries
                if book_list[r].get("title") > book_list[r + 1].get("title"):
                    book_list[r] = placeholder2
                    book_list[r + 1] = placeholder1

    return book_list


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Fisher Walsh
# P3 - sort_books_ascending_rate

def sort_books_ascending_rate(dictionary: dict) -> list:
    """
    Takes a dictionary of books sorted according to their categories as an
    argument. Returns a list of books, sorted according to their ratings in
    ascending order. For books with the same name, they are sorted
    alphabetically by their title.

    >>> sort_books_rate({'Fiction': [{'title': 'Being a book', 'rating': 3}, {'title': 'A good book', 'rating': 4.5}], 'Fantasy': [{'title': 'A book', 'rating': 3}]})
    [{'title': 'A book', 'rating': 3.7, 'categories': 'Fantasy'}, {'title': 'Being a book', 'rating': 3.7, 'categories': Fiction}, {'title': 'A good book', 'rating': 4.8, 'categories': 'Fiction'}]
    """
    
    book_list = books_to_list(dictionary)    # Converts dictionary of books to list of books
    swapping = True    # The algorithm is currently sorting
    while(swapping):    # While the algorithm is sorting
        swapping = False    # If not changed later in the execution, the algorithm does not need to sort anymore
        for i in range(len(book_list) - 1):    # For each element in the list of books
            if book_list[i].get('rating') > book_list[i + 1].get('rating') or book_list[i + 1].get('rating') == 'N/A':    #If the rating of the book at a specific index is higher than the rating of the book one index above it
                book_list[i], book_list[i + 1] = book_list[i + 1], book_list[i]    # Swap the positions of the books
                swapping = True    # Algorithm has not finished sorting
            elif book_list[i].get('rating') == book_list[i + 1].get('rating'):    # If the books have the same rating
                if book_list[i].get('title') > book_list[i + 1].get('title'):    # If the title of the book is in higher alphabetical order than the one an index in front of it
                    book_list[i], book_list[i + 1] = book_list[i + 1], book_list[i]    # Swap the positions of the books
                    swapping = True    # Algorithm has not finished sorting
    return book_list    # Returns the sorted list of books

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Main Script - Automated Testing

if __name__ == "__main__":
    total_tests = 0    # Used to keep track of the total number of tests
    tests_passed = 0    # Used to keep track f the total tests passed
    
    # Steven Lin
    # Testing Functions: sort_books_publisher
    # Test Function made by: Brady Thompson
    print("\n--- Testing by Steven Lin ---\n")
    
    # Regular alphabetical order by publisher
    print("Test 1: Alphabetical order by publisher")
    desc = "sort_books_publisher({'aerospace': [{'title': 'space exploration', 'author': 'billy', 'language': 'english', 'rating': 3.8, 'publisher': 'nasa', 'pages': 320}, {'title': 'spacex', 'author': 'elon musk', 'language': 'english', 'rating': 4.0, 'publisher': 'spacex', 'pages': 200}]})"
    
    act = sort_books_publisher({'aerospace': [{'title': 'space exploration', 'author': 'billy', 'language': 'english', 'rating': 3.8, 'publisher': 'nasa', 'pages': 320}, {'title': 'spacex', 'author': 'elon musk', 'language': 'english', 'rating': 4.0, 'publisher': 'spacex', 'pages': 200}]})
    
    ex = [{'title': 'space exploration', 'author': 'billy', 'language': 'english', 'rating': 3.8, 'publisher': 'nasa', 'pages': 320, 'category': 'aerospace'}, {'title': 'spacex', 'author': 'elon musk', 'language': 'english', 'rating': 4.0, 'publisher': 'spacex', 'pages': 200, 'category': 'aerospace'}]
    
    tests_passed += check_equal(desc, act, ex)
    total_tests += 1
    
    # Alphabetical order with duplicate books - therefore, the same author
    print("Test 2: Alphabetical order with duplicate books")
    desc = "sort_books_publisher({'animations': [{'title': 'goofy goobers','author': 'spongebob','language': 'english', 'rating': 5.0, 'publisher': 'spongebob', 'pages': 52}, {'title': 'goofy goobers','author': 'spongebob','language': 'english', 'rating': 5.0, 'publisher': 'spongebob', 'pages': 52}]})"
    
    act = sort_books_publisher({'animations': [{'title': 'goofy goobers','author': 'spongebob','language': 'english', 'rating': 5.0, 'publisher': 'spongebob', 'pages': 52}, {'title': 'goofy goobers','author': 'spongebob','language': 'english', 'rating': 5.0, 'publisher': 'spongebob', 'pages': 52}]})
    
    ex = [{'title': 'goofy goobers', 'author': 'spongebob', 'language': 'english', 'rating': 5.0, 'publisher': 'spongebob', 'pages': 52, 'category': 'animations'}]
    
    tests_passed += check_equal(desc, act, ex)
    total_tests += 1
    
    # Given the same book with different categories, should have sublists
    print ("Test 3: Same book, different categories")
    desc = "sort_books_publisher({'construction': [{'title': 'how to build a house','author': 'bob the builder','language': 'english', 'rating': '5.0', 'publisher': 'bob the builder', 'pages': '50'}], 'education': [{'title': 'how to build a house','author': 'bob the builder','language': 'english', 'rating': '5.0', 'publisher': 'bob the builder', 'pages': '50'}]})"
    
    act = sort_books_publisher({'construction': [{'title': 'how to build a house','author': 'bob the builder','language': 'english', 'rating': '5.0', 'publisher': 'bob the builder', 'pages': '50'}], 'education': [{'title': 'how to build a house','author': 'bob the builder','language': 'english', 'rating': '5.0', 'publisher': 'bob the builder', 'pages': '50'}]})
    
    ex = [{'title': 'how to build a house', 'author': 'bob the builder', 'language': 'english', 'rating': '5.0', 'publisher': 'bob the builder', 'pages': '50', 'category': ['construction', 'education']}]
    
    tests_passed += check_equal(desc, act, ex)
    total_tests += 1
    
    # Given the same publisher but different books, should order alphabetically by the title
    print ("Test 4: Same author, different books")
    desc = "sort_books_publisher({'animals': [{'title': 'penguins', 'rating': '4.9', 'publisher': 'the animal kingdom', 'pages': '200'}, {'title': 'koalas', 'rating': '5.0', 'publisher': 'the animal kingdom', 'pages': '201'}]})"
    
    act = sort_books_publisher({'construction': [{'title': 'penguins', 'rating': '4.9', 'publisher': 'the animal kingdom', 'pages': '200'}, {'title': 'koalas', 'rating': '5.0', 'publisher': 'the animal kingdom', 'pages': '201'}]})
    
    ex = [{'title': 'koalas', 'rating': '5.0', 'publisher': 'the animal kingdom', 'pages': '201', 'category': 'construction'}, {'title': 'penguins', 'rating': '4.9', 'publisher': 'the animal kingdom', 'pages': '200', 'category': 'construction'}]
    
    tests_passed += check_equal(desc, act, ex)
    total_tests += 1
    
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------
    # Brady Thompson
    # Testing done on: sort_books_author
    # Test Function made by: Nolan Wrigley
    print("\n--- Testing by Brady Thompson ---\n")
    
    #broken into a, b, c components for legibility
    # a = description, b = outcome, c = expected
    
    #alphabetize by author
    print("Author alphabetization test ---")
    a = "sort_books_author({'economics':[{'title': 'rich dad poor dad', 'author': 'john'}, {'title': 'the gamestop short squeeze', 'author': 'adam'}]})"
    b = sort_books_author({'economics':[{'title': 'rich dad poor dad', 'author': 'john'}, {'title': 'the gamestop short squeeze', 'author': 'adam'}]})
    c = [{'title': 'the gamestop short squeeze', 'author': 'adam', 'category': 'economics'}, {'title': 'rich dad poor dad', 'author': 'john', 'category': 'economics'}]
    tests_passed += check_equal(a, b, c)
    total_tests += 1
    
    #fallback: alphabetize by title if same author
    print("Fallback title alphabetization test ---")
    a = "sort_books_author({'music':[{'title': 'zz-top a history', 'author': 'music man'}, {'title': 'all about pink floyd', 'author': 'music man'}]})"
    b = sort_books_author({'music':[{'title': 'zz-top a history', 'author': 'music man'}, {'title': 'all about pink floyd', 'author': 'music man'}]})
    c = [{'title': 'all about pink floyd', 'author': 'music man', 'category': 'music'}, {'title': 'zz-top a history', 'author': 'music man', 'category': 'music'}]
    tests_passed += check_equal(a, b, c)
    total_tests += 1
    
    #create category sublists in output if same title
    print("Category sublist generation test ---")
    a = "sort_books_author({'self-improvement':[{'title': 'atomic habits', 'author': 'james clear'}], 'buisness'[{'title': 'atomic habits', 'author': 'james clear'}]})"
    b = sort_books_author({'self-improvement':[{'title': 'atomic habits', 'author': 'james clear'}], 'buisness': [{'title': 'atomic habits', 'author': 'james clear'}]})
    c = [{'title': 'atomic habits', 'author': 'james clear', 'category': ['self-improvement', 'buisness']}]
    tests_passed += check_equal(a, b, c)
    total_tests += 1
    
    #dictionary with 1 element
    print("The what if there's ony 1 book test ---")
    a = "sort_books_author({'instructional':[{'title': 'reading books for dummies', 'author': 'wiley'}]})"
    b = sort_books_author({'instructional':[{'title': 'reading books for dummies', 'author': 'wiley'}]})
    c = [{'title': 'reading books for dummies', 'author': 'wiley', 'category': 'instructional'}]
    tests_passed += check_equal(a, b, c)
    total_tests += 1
    
    #2 identical books
    print("2 identical books test ---")
    a = "sort_books_author({'mental health':[{'title': 'being unique', 'author': 'han solo'}, {'title': 'being unique', 'author': 'han solo'}]})"
    b = sort_books_author({'mental health':[{'title': 'being unique', 'author': 'han solo'}, {'title': 'being unique', 'author': 'han solo'}]})
    c = [{'title': 'being unique', 'author': 'han solo', 'category': 'mental health'}]
    tests_passed += check_equal(a, b, c)    
    total_tests += 1
    
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    # Nolan Wrigley
    # Testing of function: sort_books_ascending_rate
    # Test Function made by: Fisher Walsh
    print("\n--- Testing by Nolan Wrigley ---\n")
    
    # Checks books with the same rating to see if sorted alphabetically by title
    tests_passed += check_equal("sort_books_ascending_rate", sort_books_ascending_rate({'Category': [{'title': "Book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}, {'title': "Another book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}, {'title': "Yet another book that exists", "author": "Author that exists", "language": "English", "rating": 4.0, "publisher": "Publisher that exists", "pages": 250}]}), [{'title': "Yet another book that exists", "author": "Author that exists", "language": "English", "rating": 4.0, "publisher": "Publisher that exists", "pages": 250, 'category': "Category"}, {'title': "Another book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250, 'category': "Category"}, {'title': "Book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250, 'category': "Category"}])
    total_tests += 1
    
    """
    # Checks to make sure books with rating "N/A" appear first
    tests_passed += check_equal("sort_books_ascending_rate", sort_books_ascending_rate({'Category': [{'title': "Book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}, {'title': "Another book that exists", "author": "Author that exists", "language": "English", "rating": 4.0, "publisher": "Publisher that exists", "pages": 250}, {'title': "Yet another book that exists", "author": "Author that exists", "language": "English", "rating": "N/A", "publisher": "Publisher that exists", "pages": 250}]}), [{'title': "Yet another book that exists", "author": "Author that exists", "language": "English", "rating": 4.0, "publisher": "Publisher that exists", "pages": 250, 'category': "Category"}, {'title': "Another book that exists", "author": "Author that exists", "language": "English", "rating": 4.0, "publisher": "Publisher that exists", "pages": 250, 'category': "Category"}, {'title': "Book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250, 'category': "Category"}])
    total_tests += 1
    """
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Fisher Walsh
    # Testing done on: sort_books_title
    # Test Function made by: Steven Lin
    print("\n--- Testing by Fisher Walsh ---\n")

    
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------
    # Outputs the number of tests passed & failed
    print("\n\nTests passed:", tests_passed, "\nTests failed:", (total_tests - tests_passed)) 