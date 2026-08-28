**Library Book Search System**


**1. Objective**

To develop a Python-based library book search system that searches for a particular book from 10,00,000 books arranged in increasing order of book number and determines whether the required book exists and, if it exists, identifies its location.


**2. Input**

**The program accepts:**

Total number of books

Book numbers arranged in increasing order

Book number to be searched

For this problem:

Total number of books = 10,00,000

Book number to be searched = 75,000


**3. Output**

**The program displays:**

Whether the required book exists or not

The book number if it exists

The location/position of the book if it exists


**4. Algorithm**

1.Start.

2.Set the total number of books to 10,00,000.

3.Set the book number to be searched as 75,000.

4.Set low = 1 and high = 10,00,000.

5.Find the middle position using:
Middle = (Low + High) // 2

6.Compare the middle book number with the required book number.

If the middle book number is equal to 75,000:

The book exists.

Display the book number and its location.

7.If the required book number is smaller than the middle book number:

Search in the left half.

Set high = mid - 1.

8.If the required book number is greater than the middle book number:

Search in the right half.

Set low = mid + 1.

9.Repeat the search until the book is found or low > high.

If low > high, display "Book does not exist."

10.Stop.


**5. Time Complexity**

O(log n)

Where n is the number of books.

Since the books are arranged in increasing order, Binary Search is used. In each step, the search area is reduced by half.

For 10,00,000 books, Binary Search requires approximately 20 comparisons in the worst case.

Therefore, the overall time complexity is O(log n).
