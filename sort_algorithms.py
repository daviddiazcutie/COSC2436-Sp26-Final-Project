def selection_sort(books):
  n = len(books)
  for i in range(n - 1):
      min_idx = i
      for j in range(i + 1, n):
        if books[j]['rating'] < books[min_idx]['rating']:
            min_idx = j
        books[i], books[min_idx] = books[min_idx], books[i]

