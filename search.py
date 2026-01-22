import time
from typing import Dict, List, Optional
def linear_search(books: List[Dict], target_isbn: str) -> Optional[Dict]:
  """Perform linear search for a book by ISBN."""
  start_time = time.time()
  
  for book in books:
    if str(book['isbn']) == target_isbn:
      end_time = time.time()
      print(f"Linear Search Time: {(end_time - start_time) * 1000:.6f} ms")
      return book
  end_time = time.time()
  print(f"Linear Search Time: {(end_time - start_time) * 1000:.6f} ms")
  return None
  
def binary_search(books: List[Dict], target_isbn: str) -> Optional[Dict]:
  """Perform binary search for a book by ISBN."""
  start_time = time.time()
  left = 0
  right = len(books) - 1
  
  while left <= right:
    mid = (left + right) // 2
    current_isbn = str(books[mid]['isbn'])
    
    if current_isbn == target_isbn:
      end_time = time.time()
      print(f"Binary Search Time: {(end_time - start_time) * 1000:.6f} ms")
      return books[mid]
    elif current_isbn < target_isbn:
      left = mid + 1
    else:
      right = mid - 1
      
  end_time = time.time()
  print(f"Binary Search Time: {(end_time - start_time) * 1000:.6f} ms")
  return None

