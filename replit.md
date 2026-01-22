# Replit.md

## Overview

This is an educational Python project demonstrating search algorithm implementations. The project compares linear search and binary search algorithms for finding books by ISBN in a dataset. It serves as a learning exercise for understanding algorithm efficiency, time complexity, and Python implementation patterns.

The project includes:
- Search algorithm implementations (linear and binary search)
- A book dataset in JSON format
- A main driver program to test and compare both algorithms
- A lab report template for documenting findings

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Components

**Search Module (`search.py`)**
- Contains two search algorithm implementations
- Uses Python typing for type hints (`List`, `Dict`, `Optional`)
- Includes built-in timing measurements to compare performance
- Linear search: O(n) time complexity, works on unsorted data
- Binary search: O(log n) time complexity, requires sorted data

**Main Driver (`main.py`)**
- Loads book data from JSON files
- Runs test cases for both search algorithms
- Uses assertions for basic validation
- Sorts data before binary search (required for algorithm to work)

**Data Layer**
- Books stored in JSON format (`books.json`, `data/books.json`)
- Each book has properties: isbn, title, author, rating, description, genres, pages, publisher, etc.
- ISBN serves as the search key

### Design Decisions

1. **Timing Built Into Search Functions**
   - Problem: Need to compare algorithm performance
   - Solution: Each search function measures and prints its own execution time
   - Pros: Easy to see performance differences, self-contained
   - Cons: Mixes output concerns with search logic

2. **Type Hints Throughout**
   - Problem: Code clarity and documentation
   - Solution: Use Python's `typing` module for function signatures
   - Pros: Better IDE support, clearer interfaces, easier maintenance

3. **JSON for Data Storage**
   - Problem: Need simple, portable data format
   - Solution: Store book data in JSON files
   - Pros: Human-readable, no database setup needed, easy to edit
   - Cons: Loads entire dataset into memory, not suitable for large datasets

## External Dependencies

### Standard Library Only
- `json` - For reading book data from JSON files
- `time` - For measuring search algorithm performance
- `typing` - For type hints (`List`, `Dict`, `Optional`)

### Data Files
- `books.json` - Small test dataset with 5 books
- `data/books.json` - Larger dataset with book metadata (partial file shown)

No external packages, databases, or third-party services are used. This is a self-contained educational project.