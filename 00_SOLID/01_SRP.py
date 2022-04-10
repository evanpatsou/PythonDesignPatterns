"""
The single responsibility principle. If you have a
class it should have a primary responsibility and it should not
take other responsibilities.
"""

class Book:
    """The class represent a book"""
    
    def __init__(self):
        """Constructor of the class""" 
        self.pages = []
        self.no_pages = 0
    
    def add_page(self, content: str):
        """
        _summary_: Add a page to the book.

        Args:
            content (str): The content of the page.
        """
        self.no_pages += 1
        self.pages.append(content)
    
    def remove_page(self, position: int):
        """
        _summary_: Remove a page from the book.

        Args:
            position (int): The position of the page to be removed.
        """
        del self.pages[position]
        self.no_pages -= 1
    
    def __str__(self):
        return '\n'.join(self.pages)
    
class StorageManager:
    """
    _summary_: This class is responsible for the loading and storaging the books.
    """

    @staticmethod
    def save(book: Book, filename: str):
        """
        _summary_: Save the pages of the book.

        Args:
            book (Book): The book to save.
            filename (str): The name of the file to save.
        """
        with open(filename, 'w') as filehandle:
            for page in book.pages:
                filehandle.write('%s;' % page)
                
    @staticmethod
    def load(filename: str) -> Book:
        """
        _summary_: Load the pages of the book.

        Args:
            filename (str): The name of the file to load.
            
        Returns:
            Book: Returns the loaded book.
        """
        book = Book()
        with open(filename) as f: 
            pages = f.readlines()
            for page in pages[0].split(';'):
                book.add_page(page)
            
        return book
    
# Create a book
b = Book()
b.add_page('page 1')
b.add_page('page 2')
b.add_page('page 3')
b.add_page('page 4')
print(f'Book pages: \n{b}')
print()

# Use storage
storage = StorageManager()
storage.save(b, 'book.txt')

# Load the book
book = storage.load('book.txt')
print(f'Loaded pages: \n{book}') 
