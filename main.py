import json
import time
from search_algorithms import binary_search
from sort_algorithms import selection_sort

def load_books(filename):
    with open(filename, 'r') as file:
        books = json.load(file)

    # Ensure all books have a rating, defaulting to 0 if not provided
    for book in books:
        if 'rating' not in book:
            book['rating'] = 0.0

    return books

def display_books(books, count):
    for i in range(min(count, len(books))):
        print(f"{books[i]['title']} (Rating: {books[i]['rating']})")

def main():
    # Load dataset
    books = load_books('data/books.json')

    # Extract sorted titles for binary search
    sorted_titles = [book['title'] for book in books]

    # Binary search prompt
    print("\n---- Chapter 1: Binary Search ----")
    book_to_search = input("Enter the title of the book you want to search for: ")

    # Measure the time taken for the search
    start_search_time = time.time()
    index = binary_search(sorted_titles, book_to_search)
    end_search_time = time.time()

    search_time_taken = end_search_time - start_search_time

    if index != -1:
        print(f"Book '{book_to_search}' found at index {index}.")
    else:
        print(f"Book '{book_to_search}' not found.")

    print(f"Search took {search_time_taken:.6f} seconds.")

    # Display first 20 books before sorting by rating
    print("\n---- Displaying the first 20 books before sorting ----")
    display_books(books, 20)

    # Sort books by rating using selection sort
    print("\n---- Chapter 2: Selection Sort by Rating ----")