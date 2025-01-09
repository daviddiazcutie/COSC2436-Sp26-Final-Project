import json
import time
from search_algorithms import binary_search

# Load the books dataset
def load_books(filename):
    with open(filename, 'r') as file:
        books = json.load(file)
    return books

# Extract book titles and sort them
def extract_titles(books):
    book_titles = sorted([book['title'] for book in books])
    return book_titles

def main():
    # Load dataset
    books = load_books('data/books.json')
    book_titles = extract_titles(books)

    print("\n---- Chapter 1: Binary Search ----")
    print("Enter the title of the book you want to search for: ", end="")
    book_to_search = input().strip()

    # Measure the time taken for the search
    start_time = time.time()
    index = binary_search(book_titles, book_to_search)
    end_time = time.time()
    time_taken = end_time - start_time

    if index != -1:
        print(f"Book '{book_to_search}' found at index {index}.")
    else:
        print(f"Book '{book_to_search}' not found.")
    print(f"Search took {time_taken:.6f} seconds.")

if __name__ == "__main__":
    main()