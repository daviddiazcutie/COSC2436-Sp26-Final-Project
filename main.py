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
    
    test_isbn = "9780060809249"
    # Perform linear search
    print("\nPerforming Linear Search...")
    result = linear_search(books, test_isbn)
    if result:
        print(f"Found: {result['title']}")
    else:
        print("Book not found")
    # Sort books for binary search
    print("\nSorting books for Binary Search...")
    books.sort(key=lambda x: str(x['isbn']))
    # Perform binary search
    print("\nPerforming Binary Search...")
    result = binary_search(books, test_isbn)
    if result:
        print(f"Found: {result['title']}")
    else:
        print("Book not found")

if __name__ == "__main__":
    main()
