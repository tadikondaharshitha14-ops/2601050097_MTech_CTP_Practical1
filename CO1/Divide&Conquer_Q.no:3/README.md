**DIVIDE AND CONQUER:**

**3. Finding Maximum Temperature**
   
A weather station has temperature readings for a very large number of
days.

**Question:** Design a divide-and-conquer approach to find the maximum
temperature. 

**Solution:**

Based on the given scenarioe,the suitable divide and conquer approach to find the maximum temperature is "Merge Sort".

Merge Sort is a divide and conquer sorting algorithm.

It works in the Three basic steps:

*Divide

*Conquer

*Combine

**EXAMPLE:**

Imagine a weather station records the temperature for 8 days.

Temperature Readings:

32°C, 28°C, 35°C, 31°C, 39°C, 36°C, 30°C, 34°C

Now , divide the given temperature readings into two halfs like left half and right half.


             [32, 28, 35, 31, 39, 36, 30, 34]
                           |
                         DIVIDE
                       /         \
                      /           \
          [32, 28, 35, 31]     [39, 36, 30, 34]
                |                      |
              DIVIDE                 DIVIDE
             /      \               /      \
        [32, 28]  [35, 31]      [39, 36]  [30, 34]
          /  \      /  \          /  \      /  \
        [32][28]  [35][31]      [39][36]  [30][34]
          \  /      \  /          \  /      \  /
        [28,32]    [31,35]      [36,39]   [30,34]
             \       /              \       /
              \     /                \     /
          [28,31,32,35]            [30,34,36,39]
                    \              /
                     \            /
                      \          /
                 [28,30,31,32,34,35,36,39]
                             |
                         Last Element
                              ↓
                            39°C

So, by observing the temperatures, take the last temperature as maximum temperature.

**Maximum Temperature:**

Maximum Temperature = 39°C

**Algorithm:**

**Steps:**

MERGE_SORT(temperature, low, high)

1) Start with the complete temperature array:

[32, 28, 35, 31, 39, 36, 30, 34]

2) If low < high, find the middle:

mid = (low + high) // 2

3) Divide the array into two halves:

Left half  = low to mid
Right half = mid + 1 to high

4) Recursively apply Merge Sort to the left half.

5) Recursively apply Merge Sort to the right half.

6) Merge the two sorted halves.

7) Continue until the complete array is sorted.

8) After sorting, take the last element as the maximum temperature.

9) Return the maximum temperature.



