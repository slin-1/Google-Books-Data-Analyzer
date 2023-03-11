# T008_P2_add_remove_search_dataset
# Version 1.0 11/04/22
# Developed by: Steven Lin, Brady Thompson, Nolan Wrigley, and Fisher Walsh


# Imports
from load_data import category_dictionary
from check_equal import check_equal

# --------------------------------------------------------------------------------------------------------------------------------------------------
# The eight functions from P2 - Task 1

# Steven Lin
# P2 - add_book & remove_book functions

def add_book(dictionary: dict, book: tuple) -> dict:
    """
    Returns a dictionary with a new book, and displays whether the 
    book has been added or not depending on the number of elements in the book.
    
    >>> add_book(category_dictionary("google_books_dataset.csv"), ('Icecream Trends', 'Steven', 'English', 'Steven Inc.', 'Economics', '5.0', '52'))
    The book has been added correctly
    {... 'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 0.0, 'publisher': 'AMACOM', 'pages': 112}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'pages': 288}, {'title': 'The Power of Habit: Why We Do What We Do in Life and Business', 'author': 'Charles Duhigg', 'language': 'English', 'rating': 4.1, 'publisher': 'Random House', 'pages': 416}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 0.0, 'publisher': 'AMACOM', 'pages': 112}, {'title': 'Getting Things Done: The Art of Stress-Free Productivity', 'author': 'David Allen', 'language': 'English', 'rating': 4.5, 'publisher': 'Penguin', 'pages': 352}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176}, {'title': 'Rework', 'author': 'Jason Fried', 'language': 'English', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 0.0, 'publisher': 'AMACOM', 'pages': 112}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'language': 'English', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'language': 'English', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'language': 'English', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'language': 'English', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'language': 'English', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'language': 'English', 'rating': 0.0, 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 0.0, 'publisher': 'AMACOM', 'pages': 112}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'language': 'English', 'rating': 0.0, 'publisher': 'AMACOM', 'pages': 320}, {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'language': 'English', 'rating': 4.0, 'publisher': 'Red Wheel/Weiser', 'pages': 288}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288}, {'title': 'Icecream Trends', 'author': 'Steven', 'language': 'English', 'rating': 5.0, 'publisher': 'Steven Inc.', 'pages': 52}]...}
    
    >>> add_book(category_dictionary("google_books_dataset.csv"), ('Sample Book 1', 'Steven', 'English', 'Steven Inc.', 'New Category', '1.0', '100'))
    The book has been added correctly
    {... 'New Category': [{'title': 'Sample Book', 'author': 'Steven', 'language': 'English', 'rating': 1.0, 'publisher': 'Steven Inc.', 'pages': 100}]}
    
    >>> add_book(category_dictionary("google_books_dataset.csv"), ('Sample Comic', '100.0', 'English', 'Steven Inc.', 'Comics', '5.0', '100', 'test_fail'))
    There was an error adding the book
    {... 'Information Technology': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': 'English', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464}], 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30}]}
    """
    
    lst_book = []      # Empty list to hold the new book before being moved into a dictionary
    categories = []    # Empty list to hold the categories
    new_book = {}      # Empty dictionary to hold the new book
    
    if len(book) > 7 or len(book) < 7:    # Returns the original dictionary if the length of the book tuple is greater or less than 7 elements
        print("There was an error adding the book") 
        return dictionary
    
    title, author, language, publisher, category, rating, pages = book    # Unpacks the tuple to later add to a list
    
    lst_book.append(title)        # Add title to the list 'lst_book'
    lst_book.append(author)       # Add author to the list 'lst_book'
    lst_book.append(language)     # Add language to the list 'lst_book'
    lst_book.append(publisher)    # Add publisher to the list 'lst_book'
    lst_book.append(category)     # Add category to the list 'lst_book'
    lst_book.append(rating)       # Add rating to the list 'lst_book'
    lst_book.append(pages)        # Add pages to the list 'lst_book'

    if lst_book[5] != '':    # Convert ratings to a float if not empty
        lst_book[5] = float(lst_book[5])
    if lst_book[6] != '':    # Convert pages to an int if not empty
        lst_book[6] = int(lst_book[6])    
    
    categories.append(lst_book[4])    # Adds the categories to the categories list
    lst_book.pop(4)    # Removes the categories for the list of data    
    
    new_book.update({"title": lst_book[0]})        # Add the title
    new_book.update({"author": lst_book[1]})       # Add the author
    new_book.update({"language": lst_book[2]})     # Add the language
    new_book.update({"rating": lst_book[4]})       # Add the rating
    new_book.update({"publisher": lst_book[3]})    # Add the publisher
    new_book.update({"pages": lst_book[5]})        # Add the pages    
    
    if categories[0] in dictionary.keys():    # Checking to see if the new book category is in the dictionary
        if new_book not in dictionary.get(categories[0]):    # Checking if the new_book value is not in the current category
            dictionary.update({categories[0]:dictionary.get(categories[0]) + [new_book]})    # Adds the previous values and the current temp_dict value to the key (category) position 
            print("The book has been added correctly")
    else:
        dictionary.update({categories[0]:[new_book]})    # Add a new category and assign the current new_book value
        print("The book has been added correctly")
        
    return dictionary


def remove_book(dictionary: dict, book_title: str, book_category: str) -> dict:
    """
    Returns an updated dictionary with a book removed and displays whether the 
    book has been removed or not.
    
    >>> remove_book(category_dictionary("google_books_dataset.csv"), "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction')
    The book has been removed correctly
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'pages': 416}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'language': 'English', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'language': 'English', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'language': 'English', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': 'English', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'language': 'English', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'language': 'English', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'language': 'English', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'language': 'English', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'language': 'English', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'language': 'English', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}]...
    
    >>> remove_book(category_dictionary("google_books_dataset.csv"), 'Sample Comic', 'Comics')
    There was an error removing the book. Book not found.
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'pages': 416}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'language': 'English', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'language': 'English', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'language': 'English', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': 'English', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'language': 'English', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'language': 'English', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'language': 'English', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'language': 'English', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'language': 'English', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'language': 'English', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}]...
    """
    
    categories = dictionary.get(book_category)    # Attempts to obtain the desired category from the dictionary
    titles = []    # Empty list to hold the dictionary book titles
    diction_values = []    # Empty list to hold the dictionary values
    diction_values += dictionary.values()    # Obtain all the dictionary values

    if categories == None:    # Check if the category is in the dictionary
        print("There was an error removing the book. Book not found.")    # Indicates that the book is not found, as the category does not exist
        return dictionary
    
    for a in range(len(dictionary)):    
        for b in range(len(diction_values[a])):
            titles.append(diction_values[a][b].get('title'))    # Adds all the titles to the 'titles' list

    if book_title not in titles:    # Checks if the desired book title is in the 'titles' list
        print("There was an error removing the book. Book not found.")    # Indicates that the book is not found, as the title does not exist
        return dictionary
    
    for c in range(len(titles)):    # Loops through the titles
        for d in range(len(categories)):    # Loops through the content in the specific category
            if book_title == titles[c]:    # Checks if the desired book title matches the current title
                categories.pop(d)    # Removes the book with the matching title
                print("The book has been removed correctly")    # Indicates that the book has been removed
                return dictionary
    
    print("There was an error removing the book. Book not found.")
    return dictionary    # Returns the provided dictionary with no changes if all else fails

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Brady Thompson
# get_books_by_category & get_books_by_rate

def get_books_by_category(dictionary:dict, category:str) -> int: 
    """lists out a how many items of a certain category are in a
    dictionary. Also returns how many items
    
    >>> get_books_by_category({'Home-repair': [{'title': 'art of cleanliness', 'author': 'Marie-Kondo}, {'title': 'build a house: 6 simple steps', 'author': 'ben hur'}]}, 'Home-repair')
    The category "Home-repair" has 2 books. This is the list of books:
    Book 1: "art of cleanliness" by "Marie Kondo"
    Book 2: "build a house: 6 simple steps" by "ben hur"
    >>> get_books_by_category({'category': [{'title': 'example', 'author': 'expample'}]}, 'missing category')
    The category "missing category" is not in the list of blooks!
    >>> get_books_by_category({'geology': 17}, 'geology')
    Invalid Dictionary. Should be category-sorted
    """
    
    x = dictionary.get(category)
    if x == None: #ensure category exists
        print('The category "{}" is not in the list of books! Or the dictionary is improperly sorted!'.format(category))
        return None
    if type(x).__name__ != "list": #ensure we're going to iterate on a list from the dictionary
        print("Invalid dictionary. Should be category-sorted")
        return
    
    print("The category", category, "has", len(x), "books. This is the list of books:")
    n = 0
    for item in x: #loop through list, picking out values for title and author to print it out to a list of items in the list.
        n += 1
        a,b,c,d,e,f=item.values()
        print('Book {}: "{}" by "{}"'.format(n, a, b))
    return n


def get_books_by_rate(dictionary: dict, rate: float) -> int:
    """Returns the number of books for the given rate (between rate and rate +1)
    prints info about each book
    ;;precindition: dictionary list is formatted
    ;;based on the output of category_dictionary
    
    >>> get_books_by_rate({'Fiction': [{'title': 'How to win friends and influence people', 'author': 'that guy', '': '', 'rate': 4.5}]}, 4)
    There are 1 books whose rate is between 4 and 5. This is the list of books:
    Book 1: "How to win friends and influence people" by "that guy
    >>> get_books_by_rate({#dictionary of terrible books, 4}
    There are no books within +1 of specified rate
    """
    
    #some of this code is borrowed from get_books_by_category()
    keylist = list(dictionary.keys()) #find all categories of book
    
    #create list of books of specific rate
    inrangelist = set() #set so that duplicates are automatically removed
    for individualkey in keylist: #find all books from each category
        categorybooks = dictionary.get(individualkey)
        for book in categorybooks: #iterate through each book from each category
            a, b, c, d, e, f = book.values()
            if d != "" and rate <= d < (rate + 1): #quit early if "" only pass if within range of acceptable ratings
                inrangelist.add((a, b)) #add book to set of title/author tuples
    
    #print # of books between range
    print("There are {} books whose rate is between {} and {}. This is the list of books:".format(len(inrangelist), rate, (rate + 1)))
    n = 0
    for item in inrangelist: #print info on each book
        n += 1
        a, b = item
        print('Book {}: "{}" by "{}"'.format(n, a, b))
    if n == 0: #debug to show that there were no books found
        print("there were no items within +1 of specified rate")
    return n

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Nolan Wrigley
# get_books_by_title & get_books_by_author

def get_books_by_title(dictionary: dict, book_title: str) -> bool:
    """
    Takes in the given dictionary and returns True if the given book_title is present amoung it or False if the book_title is not present
    
    >>> get_books_by_title(category_dictionary("google_books_dataset.csv"), "How To Win Friends and Influence People")
    The book has been found
    True
    
    >>> get_books_by_title(category_dictionary("google_books_dataset.csv"), "The Painted Man (The Demon Cycle. Book 1)")
    The book has been found
    True
    
    >>> get_books_by_title(category_dictionary("google_books_dataset.csv"), "Deadpool Kills the Marvel Universe")
    The book has been found
    True
    
    >>> get_books_by_title(category_dictionary("google_books_dataset.csv"), "2Pac's greatest hits")
    The book has NOT been found
    False
    """
    diction = []                    # "diction" is created as a list as to not have diction be a dict entry
    diction += dictionary.values()  # Adds all of the dictions from each category to the list diction
    
    titles = []                                         # Creates an empty list that will become a list with every title in the dictionary
    for i in range(len(dictionary)):                     
        for j in range(len(diction[i])):                
            titles.append(diction[i][j].get('title'))   # Adds every title present in the diction list to a new list, "titles"
            
    for k in range(len(titles)):                
        if book_title == titles[k]:             # If the passed in "book_title" is present anywhere in the "titles" list, the if statement will be true
            print("The book has been found")    # Prints to the console that the book has been found if the book is present in the dictionary
            return True                         # Returns a value of True if the book has been found
    print("the book has NOT been found")        # If the passed in "book_title" is not present anywhere in the "titles" list, the print statement will print
    return False                                # Returns a value of False if the book has not been found
    
    
def get_books_by_author(dictionary: dict, author: str) -> str:
    """
    Returns a string with all of the unique books an author has written from a given dictionary.
    
    >>> get_books_by_author(category_dictionary("google_books_dataset.csv"), "Barbara Allan")
    The author Barbara Allan has published the following books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery, rate: 3.3
    Book 2: Antiques Con, rate: 4.8
    Book 3: Antiques Chop, rate: 4.5
    Book 4: Antiques Knock-Off, rate: 4.3
    
    >>> get_books_by_author(category_dictionary("google_books_dataset.csv"), "Peter V. Brett")
    The author Peter V. Brett has published the following books:
    Book 1: The Painted Man (The Demon Cycle. Book 1), rate: 4.5
    
    >>> get_books_by_author(category_dictionary("google_books_dataset.csv"), "Brandon Sanderson")
    The author Brandon Sanderson has published the following books:
    Book 1: Edgedancer: From the Stormlight Archive, rate: 4.8
    Book 2: Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages, rate: 4.7
    """
    titlerating = {} # Creates an empty dictionary that will have values of "title":"rating"
    
    diction = []                    # "diction" is created as a list as to not have diction be a dict entry
    diction += dictionary.values()  # Adds all of the dictions from each category to the list diction

    titles = []     # Creates an empty list that will have all of the titles of the passed in author
    ratings = []    # Creates an empty list that will have all of the ratings of the passed in author
    for i in range(len(dictionary)):
        for j in range(len(diction[i])):
            auth = diction[i][j].get('author')              # Creates a value that will be the current author present in the current diction set
            if author == auth:                              # If the passed in author is the same as the one present in the diction ,the if statement will be true
                titles.append(diction[i][j].get('title'))   # Adds the title of the book to the the list "titles"
                ratings.append(diction[i][j].get('rating')) # Adds the rating of the book to the list "ratings"
    
    for k in range(len(titles)):                    
        titlerating.update({titles[k]:ratings[k]})  # Done so duplicate entires of titles with different categories will not be listed as sets can only have unique entries
        
    print("The author", author, "has published the following books:")   # Setup print statement that will print before the return value
    
    books = ""  # Creates an empty string that will be what each book the author wrote will be added onto
    for l in range(len(titlerating)):                                                               
        books += "Book " + str(l + 1) + ": " + str(titles[l]) + ", rate: " + str(ratings[l]) + "\n" # Adds the book title and rating to the string "books"
    
    return books    # Returns the modified string "books" with all the books the author wrote along with their ratings

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Fisher Walsh
# get_books_by_publisher & get_all_categories_for_book_title

def get_books_by_publisher(books_by_category: dict, publisher: str) -> int:
    """
    Accepts a dictionary of books, sorted according to their category, and a
    name of a publisher as a string. Returns the number of books that the
    specific publisher has published as an integer. Prints relevant information,
    such as the title and author of the published book.

    >>> get_books_by_publisher({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", "..."}, {...}], '...': [...]}, "Kensington Publishing Corp.")
    #Prints:
    The publisher Kensington Publishing Corp. has published the following books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Antiques Knock-Off by Barbara Allan
    #Returns:
    2
    """
    books_by_publisher = [] #declares empty list of books that a certain publisher has published
    book_list = sum(books_by_category.values(), []) #converts the dictionary of books to a list of books
    print(f"The publisher {publisher} has published the following books:") #prints header with title of the book
    for book in book_list: #loops for each book in the list of books
        if book.get("publisher") == publisher and book not in books_by_publisher: #checks if the publisher is the desired publisher, and the book is not already in the list of books
            books_by_publisher += [book] #adds the book to the list of published books
            print(f"Book {len(books_by_publisher)}: {book.get('title')} by {book.get('author')}") #prints information such as the book number, the title, and the author
    return len(books_by_publisher) #returns the number of books

def get_all_categories_for_book_title(books_by_category: dict, title: str) -> int:
    """
    Accepts a dictionary of books, stored according to their category, and a
    book title as a string. Returns the number of categories that the book with
    the specified title belongs to. Prints relevant information, such as the
    categories the book with the specified title belongs to.

    >>> get_all_categories_for_book_title({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", "..."}, {...}], '...': [...]}, "The Vagrant (The Vagrant Trilogy)")
    #Prints:
    The book title The Vagrant (The Vagrant Trilogy) belongs to the following categories:
    Category 1: Fiction
    Category 2: Fantasy
    #Returns:
    2
    """
    categories = 0 #initializes a variable to count the number of categories a book belongs to
    print(f"The book title {title} belongs to the following categories:") #prints header with title of the book
    for category, books in books_by_category.items(): #loops for each category in the items belonging to the dictionary of books
        for book in books: #loops for each book in the books belonging to a certain category
            if book.get("title") == title: #checks if the title is the desired title
                categories += 1 #increments the counter
                print(f"Category {categories}: {category}") #prints category number and the category
    return categories #returns the number of categories


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Main Script
if __name__ == "__main__":
    total_tests = 0
    tests_passed = 0
    
    # Steven Lin
    # Testing Functions: get_books_by_category & get_books_by_rate
    # Test Functions by: Brady Thompson
    print("\n--- Testing by Steven Lin ---\n")
    
    # Test 1 - get_books_by_category - Invalid category
    tests_passed += check_equal("get_books_by_category - Invalid category", get_books_by_category({'Aerospace': [{'title': "SpaceX", "author": "Elon Musk", "language": "English", "rating": 4.0, "publisher": "SpaceX", "pages": 50}]}, 'Gorillas'), None)
    total_tests += 1
    
    # Test 2 - get_books_by_category - 2 different books, same category
    tests_passed += check_equal("get_books_by_category - 2 different books, same category", get_books_by_category({'Aerospace': [{'title': "SpaceX", "author": "Elon Musk", "language": "English", "rating": 4.0, "publisher": "SpaceX", "pages": 50}, {'title': "NASA", "author": "Bob", "language": "English", "rating": 4.5, "publisher": "SpaceX", "pages": 562}]}, 'Aerospace'), 2)
    total_tests += 1
    
    # Test 3 - get_books_by_category - 2 identical books, same category
    tests_passed += check_equal("get_books_by_category - 2 identical books, same category", get_books_by_category({'Aerospace': [{'title': "SpaceX", "author": "Elon Musk", "language": "English", "rating": 4.0, "publisher": "SpaceX", "pages": 50}, {'title': "SpaceX", "author": "Elon Musk", "language": "English", "rating": 4.0, "publisher": "SpaceX", "pages": 50}]}, 'Aerospace'), 2)
    total_tests += 1
    
    # Test 1 - get_books_by_rate - Invalid rate
    tests_passed += check_equal("get_books_by_rate - Invalid rate", get_books_by_rate({'Animals': [{'title': "Penguins", "author": "Tom", "language": "English", "rating": 5.0, "publisher": "Tom", "pages": 60}]}, 0.0), 0)
    total_tests += 1
    
    # Test 2 - get_books_by_rate - 2 different books, same rating
    tests_passed += check_equal("get_books_by_rate - 2 different books, same rating", get_books_by_rate({'Animals': [{'title': "Penguins", "author": "Tom", "language": "English", "rating": 5.0, "publisher": "Tom", "pages": 60}], 'Engineering': [{'title': "Mechanical Engineering", "author": "Billy", "language": "English", "rating": 5.0, "publisher": "Billy", "pages": 205}]}, 5.0), 2)
    total_tests += 1
    
    # Test 3 - get_books_by_rate - 2 identical books, same rating
    tests_passed += check_equal("get_books_by_rate - 2 different books, same rating", get_books_by_rate({'Animals': [{'title': "Penguins", "author": "Tom", "language": "English", "rating": 5.0, "publisher": "Tom", "pages": 60}, {'title': "Penguins", "author": "Tom", "language": "English", "rating": 5.0, "publisher": "Tom", "pages": 60}]}, 5.0), 1)
    total_tests += 1
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    # Brady Thompson
    # Testing done on get_books_by_author and get_books_by_title functions:
    # GBBA and GBBT by: Nolan Wrigley
    print("\n--- Testing by Brady Thompson --- \n")

    tests_passed += check_equal("get_books_by_title but missing title", get_books_by_title({'biography': [{'title': "Trump: the autobiography", "author": "Mike Pence", "language": "English", "rating": 4.1, "publisher": "Truth Social", "pages": 420}]},"Barack Obama biography"), False)
    total_tests += 1
    
    tests_passed += check_equal("get_books_by_title but 2 of same book", get_books_by_title({'biography': [{'title': "Trump: the autobiography", "author": "Mike Pence", "language": "English", "rating": 4.1, "publisher": "Truth Social", "pages": 420},{'title': "Trump: the autobiography", "author": "Mike Pence", "language": "English", "rating": 4.1, "publisher": "Truth Social", "pages": 420}]},"Trump: the autobiography"), True)
    total_tests += 1
    
    tests_passed += check_equal("get_books_by_author missing author", get_books_by_author({'book': [{'title': "book title", "author": "John Doe", "language": "English", "rating": 3.0, "publisher": "barnes and noble", "pages": 300}]},"John Smith"), "")
    total_tests += 1
    
    tests_passed += check_equal("get_books_by_author but same author in 2 categories", get_books_by_author({'category 1': [{'title': "book1", "author": "John", "language": "English", "rating": 5.0, "publisher": "barnes and noble", "pages": 300}], 'category 2': [{'title': "book2", "author": "John", "language": "English", "rating": 4.0, "publisher": "barnes and noble", "pages": 200}]},"John"), "Book 1: book1, rate: 5.0\nBook 2: book2, rate: 4.0\n")
    total_tests += 1

    # --------------------------------------------------------------------------------------------------------------------------------------------------

    # Nolan Wrigley
    # Testing of functions 7 and 8, get_books_by_publisher & get_all_categories_for_book_title
    # Functions made by: Fisher Walsh
    print("\n--- Testing by Nolan Wrigley ---\n")

    tests_passed += check_equal("get_books_by_publisher missing publisher", get_books_by_publisher({'Category': [{'title': "Book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}]}, "Publisher that does not exist"), 0)
    total_tests += 1

    tests_passed += check_equal("get_books_by_publisher but same book with different category", get_books_by_publisher({'Category 1': [{'title': "Book that exists 1", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}], 'Category 2': [{'title': "Book that exists 1", "author": "Author that exists 1", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}], 'Category 3': [{'title': "Book that exists 2", "author": "Author that exists 2", "language": "English", "rating": 5.0, "publisher": "Publisher that exists", "pages": 250}]},"Publisher that exists"), 3)
    total_tests += 1

    tests_passed += check_equal("get_all_categories_for_book_title missing book title", get_all_categories_for_book_title({'book': [{'title': "Book that exists", "author": "Author that exists", "language": "English", "rating": 5.0, "publisher": "Marvel Entertainment", "pages": 250}]}, "Book that does not exist"), 0)
    total_tests += 1

    tests_passed += check_equal("get_all_categories_for_book_title but same book in 2 different categories", get_all_categories_for_book_title({'Category 1': [{'title': "Book that exists 1", "author": "Author that exists 1", "language": "English", "rating": 5.0, "publisher": "Publisher that exists 1", "pages": 250}], 'Category 2': [{'title': "Book that exists 1", "author": "Author that exists 1", "language": "English", "rating": 5.0, "publisher": "Publisher that exists 1", "pages": 250}], 'Category 3': [{'title': "Book that exists 2", "author": "Author that exists 2", "language": "English", "rating": 5.0, "publisher": "Publisher that exists 2", "pages": 250}]},"Book that exists 1"), 2)
    total_tests += 1

    # --------------------------------------------------------------------------------------------------------------------------------------------------

    # Fisher Walsh
    # Testing done on add_book & remove_book functions
    # Functions developed by: Steven Lin
    print("\n--- Testing by Fisher Walsh ---\n")
    
    test_dict = {
    'Fiction':
    [{'title': "Things That Are False", 'author': "Joe Liar", 'language': "English", 'rating': 3.8, 'publisher': "Real Publishing Company", 'pages': 2342356},
    {'title': "Fantasy Book With Dragons", 'author': "Bartholomew Bunderbones", 'language': "English", 'rating': 4.1, 'publisher': "Real publishing company", 'pages': 934}],
    'Nonfiction':
    [{'title': "Things That Are True", 'author': "John Candor", 'language': "English", 'rating': 3.7, 'publisher': "Questionable Publishing Company", 'pages': 1025}],
    'Fantasy':
    [{'title': "Fantasy Book With Dragons", 'author': "Bartholomew Bunderbones", 'language': "English", 'rating': 4.1, 'publisher': "Real Publishing Company", 'pages': 934}]
    }
    
    tests_passed += check_equal("add_book | Adding a new book |", add_book(test_dict, ("Things That Have Happened", "Joe Liar", "English", "Questionable Publishing Company", "Nonfiction", "4.5", "56")), {
    'Fiction':
    [{'title': 'Things That Are False', 'author': 'Joe Liar', 'language': 'English', 'rating': 3.8, 'publisher': 'Real Publishing Company', 'pages': 2342356},
    {'title': 'Fantasy Book With Dragons', 'author': 'Bartholomew Bunderbones', 'language': 'English', 'rating': 4.1, 'publisher': 'Real publishing company', 'pages': 934}],
    'Nonfiction':
    [{'title': 'Things That Are True', 'author': 'John Candor', 'language': 'English', 'rating': 3.7, 'publisher': 'Questionable Publishing Company', 'pages': 1025},
    {'title': 'Things That Have Happened', 'author': 'Joe Liar', 'language': 'English', 'rating': 4.5, 'publisher': 'Questionable Publishing Company', 'pages': 56}],
    'Fantasy':
    [{'title': 'Fantasy Book With Dragons', 'author': 'Bartholomew Bunderbones', 'language': 'English', 'rating': 4.1, 'publisher': 'Real Publishing Company', 'pages': 934}]
    })
    total_tests += 1
    
    tests_passed += check_equal("add_book | Attempting to add a book that is already in the dictionary |", add_book(test_dict, ("Things That Are False", "Joe Liar", "English", "Real Publishing Company", "Fiction", "3.8", "2342356")), test_dict)
    total_tests += 1
    
    tests_passed += check_equal("add_book | Attempting to add a book with too many arguments |", add_book(test_dict, ("Things That Are False", "Joe Liar", "English", "Real Publishing Company", "Fiction", "3.8", "2342356", "Big Books Public Library")), test_dict)
    total_tests += 1
    
    tests_passed += check_equal("remove_book | Removing a book |", remove_book(test_dict, "Things That Are False", "Fiction"), {
    'Fiction':
    [{'title': 'Fantasy Book With Dragons', 'author': 'Bartholomew Bunderbones', 'language': 'English', 'rating': 4.1, 'publisher': 'Real publishing company', 'pages': 934}],
    'Nonfiction':
    [{'title': 'Things That Are True', 'author': 'John Candor', 'language': 'English', 'rating': 3.7, 'publisher': 'Questionable Publishing Company', 'pages': 1025},
    {'title': 'Things That Have Happened', 'author': 'Joe Liar', 'language': 'English', 'rating': 4.5, 'publisher': 'Questionable Publishing Company', 'pages': 56}],
    'Fantasy': [{'title': 'Fantasy Book With Dragons', 'author': 'Bartholomew Bunderbones', 'language': 'English', 'rating': 4.1, 'publisher': 'Real Publishing Company', 'pages': 934}]
    })
    total_tests += 1
    
    tests_passed += check_equal("remove_book | Attempting to remove a book that does not exist|", remove_book(test_dict, "Things That Aren't Not False", "Fiction"), test_dict)    
    total_tests += 1


    print("\n\nTests passed:", tests_passed, "\nTests failed:", (total_tests - tests_passed)) # Outputs the number of tests passed & failed