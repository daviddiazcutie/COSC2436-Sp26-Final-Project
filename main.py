import json
import time
from search import linear_search, binary_search
from sort_algorithms import selection_sort

def load_books(filename):
    try:
        with open(filename, 'r') as file:
            books = json.load(file)
        for book in books:
            if 'rating' not in book:
                book['rating'] = 0.0
        return books
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}!")
        return []

def display_books(books, count):
    for i in range(min(count, len(books))):
        print(f"{books[i]['title']} (Rating: {books[i]['rating']})")

def main():
    # Load dataset
    # Prioritize 'books.json' if it exists, otherwise use 'data/books.json'
    filename = 'books.json'
    books = load_books(filename)
    if not books:
        books = load_books('data/books.json')
    
    if not books:
        print("No books loaded. Exiting.")
        return

    # Extract sorted titles for binary search
    sorted_titles = sorted([book['title'] for book in books])
    
    # Binary search prompt
    print("\n---- Chapter 1: Binary Search ----")
    book_to_search = input("Enter the title of the book you want to search for: ")
    
    # Measure the time taken for the search
    start_search_time = time.time()
    # Note: search.py binary_search expects (books, target_isbn) 
    # but here it's used on titles. This might need matching search.py logic.
    # For now, following the structure provided in main.py.
    index = binary_search([{'isbn': t, 'title': t} for t in sorted_titles], book_to_search)
    end_search_time = time.time()
    
    search_time_taken = end_search_time - start_search_time
    
    if index:
        print(f"Book '{book_to_search}' found.")
    else:
        print(f"Book '{book_to_search}' not found.")
    print(f"Search took {search_time_taken:.6f} seconds.")

    # Display first 20 books before sorting by rating
    print("\n---- Displaying the first 20 books before sorting ----")
    display_books(books, 20)

    # Sort books by rating using selection sort
    print("\n---- Chapter 2: Selection Sort by Rating ----")
    start_sort_time = time.time()
    selection_sort(books)
    end_sort_time = time.time()
    
    sort_time_taken = end_sort_time - start_sort_time
    print("Books sorted by rating using selection sort.")
    print(f"Sorting took {sort_time_taken:.6f} seconds.")

    # Display first 20 books after sorting by rating
    print("\n---- Displaying the first 20 books after sorting ----")
    display_books(books, 20)

if __name__ == "__main__":
    main()
