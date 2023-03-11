# T008_P5_load_data
# Version 1.0 11/04/22
# Written by: Steven Lin
# Edited by: Brady Thompson, Fisher Walsh, Nolan Wrigley

def category_dictionary(filename: str) -> dict:    # Format: {category:[{'title': str, 'author': str, 'language': str, 'rating': float, 'publisher': str, 'pages': int}]}
    """ Precondition: the data file must not contain commas in its entries
    
    Returns a dictionary that includes the key values stored in categories and 
    their respective values as the book title, author, language, rating (out of 5), publisher, and number of pages.
    Removes duplicate entries given multiple entries within the same category.
    
    >>> category_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 672}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'pages': 416}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'language': 'English', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250}, {'title': 'A Trace of Crimme (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'language': 'English', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': 'English', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'language': 'English', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'language': 'English', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'language': 'English', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'language': 'English', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'language': 'English', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}, (new category) : [books elements], etc...}
    """
    
    hold_data = []    # Empty list to hold file data
    category_dict = {}    # Empty dictionary for the categories
    categories = []    # Empty list to hold categories
    infile = open(filename, 'r')    # Open file (e.g. "google_books_dataset.csv")
    
    for line in infile:
        hold_data += [line.replace("N/A", "0.0").strip("\n").split(",")]    # Add file data to the empty "hold_data" list
    
    hold_data.pop(0)    # Removes the first line of the dataset for formatting ("title", "author"...)
    
    for a in range(len(hold_data)):
        if hold_data[a][2] != '':    # Convert ratings to a float if not empty
            hold_data[a][2] = float(hold_data[a][2])
        if hold_data[a][4] != '':    # Convert pages to an int if not empty
            hold_data[a][4] = int(hold_data[a][4])
            
    for b in range(len(hold_data)):
        categories += hold_data[b][5].strip("\n").split(",")    # Adds the categories to the categories list
        hold_data[b].pop(5)    # Removes the categories for the list of data
    
    for c in range(len(hold_data)):
        temp_dict = {}    # Empty and temporary dictionary
        
        temp_dict.update({"title": hold_data[c][0]})    # Add the title
        temp_dict.update({"author": hold_data[c][1]})    # Add the author
        temp_dict.update({"language": hold_data[c][5]})    # Add the language
        temp_dict.update({"rating": hold_data[c][2]})    # Add the rating
        temp_dict.update({"publisher": hold_data[c][3]})    # Add the publisher
        temp_dict.update({"pages": hold_data[c][4]})    # Add the pages
        
        if categories[c] in category_dict.keys():    # Checking to see if the category has been added to the dictionary before
            if temp_dict not in category_dict.get(categories[c]):    # Checking if the temp_dict value is not in the current category
                category_dict.update({categories[c]:category_dict.get(categories[c]) + [temp_dict]})    # Adds the previous values and the current temp_dict value to the key (category) position 
        else:
            category_dict.update({categories[c]:[temp_dict]})    # Add a new category and assign the current temp_dict value
    
    infile.close()        
    return category_dict # Return the category dictionary