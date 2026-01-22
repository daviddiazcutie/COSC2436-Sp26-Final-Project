# Chapter 1 Lab Report: Search Algorithms
## Student Information
- Name: David Diaz Cutie
- Date: 01/21/2026
## Implementation Overview
In this lab, two different searching algorithms were implemented: Linear Search and Binary Search.

Linear Search: This algorithm performs a sequential search through a list, checking every entry one by one until the target is found. This makes it less efficient for large datasets, with a time complexity of O(n).

Binary Search: This algorithm uses a "divide and conquer" approach, halving the search interval in each iteration. This results in a time complexity of O(log n), making it significantly more efficient for large, sorted datasets.

## Test Results

--- Test 1: Existing Book ---
Searching for ISBN: 9780060809249
Linear Search Time: 0.001431 ms
Found: Brave New World
--- Test 2: Non-existent Book ---
Searching for ISBN: 0000000000000
Linear Search Time: 0.002146 ms
Correctly identified as not found
--- Test 3: First Book ---
Searching for first ISBN: 1111
Linear Search Time: 0.000238 ms
Found first book: Book A
Searching for last ISBN: 9781593081072
Linear Search Time: 0.000477 ms
Found last book: The Phantom of the Opera
--- Final Check: Binary Search ---
Binary searching for ISBN: 9780060809249
Binary Search Time: 0.001431 ms
Found: Brave New World

## Challenges and Solutions
One of the primary challenges encountered was ensuring the proper formatting of the JSON file and maintaining data consistency when accessing the array. I had to ensure all ISBN values were treated as strings to allow for accurate comparisons. Reviewing the official Python json documentation was necessary to resolve parsing issues.

## Learning Outcomes
Practical understanding of algorithm efficiency and speed. While both algorithms work, Binary Search is far faster for finding values in large datasets. In smaller datasets, the difference is negligible, but in large-scale projects, the efficiency of O(log n) is unequivocal.