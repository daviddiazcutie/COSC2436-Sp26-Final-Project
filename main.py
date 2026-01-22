import json
from search import linear_search, binary_search

def main():
    # Load books data
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        print("Error: books.json file not found!")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in books.json!")
        return

    print(f"Total books loaded: {len(books)}")

    # 1. Test existing book
    print("\n--- Test 1: Existing Book ---")
    test_isbn = "9780060809249" # Known to exist
    print(f"Searching for ISBN: {test_isbn}")
    result = linear_search(books, test_isbn)
    assert result is not None, "Should find existing book"
    print(f"Found: {result['title']}")

    # 2. Test non-existent book
    print("\n--- Test 2: Non-existent Book ---")
    test_isbn = "0000000000000" # Known not to exist
    print(f"Searching for ISBN: {test_isbn}")
    result = linear_search(books, test_isbn)
    assert result is None, "Should return None for non-existent book"
    print("Correctly identified as not found")

    # 3. Test first and last books
    print("\n--- Test 3: First and Last Books ---")
    # Get first ISBN
    first_isbn = str(min(book['isbn'] for book in books))
    print(f"Searching for first ISBN: {first_isbn}")
    result = linear_search(books, first_isbn)
    assert result is not None, "Should find first book"
    print(f"Found first book: {result['title']}")

    # Final check with Binary Search
    print("\n--- Final Check: Binary Search ---")
    books.sort(key=lambda x: str(x['isbn']))
    test_isbn = "9780060809249"
    print(f"Binary searching for ISBN: {test_isbn}")
    result = binary_search(books, test_isbn)
    if result:
        print(f"Found: {result['title']}")
    else:
        print("Book not found")

if __name__ == "__main__":
    main()
