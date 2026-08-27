**Maximum Agricultural Profit System**


**1. Objective**

To develop a Python-based Maximum Agricultural Profit System that analyzes the daily profit and loss of a farmer and identifies the continuous period with the maximum total profit.

The system uses the Maximum Subarray algorithm (Kadane's Algorithm) to find the most profitable continuous period.


**2. Input**

**The program accepts:**

Number of days

Daily profit or loss for each day

Here, each value represents the profit or loss for one day.


**3. Output**

**The program displays:**

Daily profit/loss values

Maximum continuous profit

The continuous period that produces the maximum profit


**4. Algorithm**

1.Start.

2.Read the number of days.

3.Read the profit or loss for each day.

4.Store the daily values in an array.

5.Initialize current_sum and maximum_sum with the first value.

6.Start traversing the array from the second day.

7.For each day's profit/loss:

Add the current value to current_sum.

Compare the current value with current_sum.

If the current value is greater, start a new subarray from the current day.

Update maximum_sum whenever current_sum becomes greater than the previous maximum.

8.Keep track of the starting and ending positions of the maximum subarray.

9.After checking all days, display the maximum continuous profit.

10.Display the corresponding profitable period.

11.Stop.


**5. Time Complexity**

O(n)

Where n is the number of days.

The algorithm traverses the list of daily profits only once. Therefore, the time complexity is O(n).
