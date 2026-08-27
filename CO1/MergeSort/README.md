**Student Scholarship Selection System**

**1. Objective**

To develop a Python-based student scholarship selection system that stores student names and marks, sorts the students in descending order of marks, and identifies students who are eligible for a scholarship based on their marks.

For this problem, a student is eligible for a scholarship if the student scores 80 marks or above.


**2. Input**

**The program accepts:**

1.Number of students

2.Student name

3.Student marks

4.Scholarship eligibility mark

**3. Output**

**The program displays:**

1.List of students sorted in descending order of marks

2.Student names and their marks

3.Students eligible for the scholarship


**4. Algorithm**

1.Start.

2.Create a list to store student names and marks.

3.Read the number of students.

4.For each student:

Read the student's name.

Read the student's marks.

5.Store the name and marks in the list.

6.Sort the list of students in descending order of marks.

7.Display all students with their marks after sorting.

8.Set the scholarship eligibility mark to 80.

9.Check each student's marks.

10.If a student's marks are greater than or equal to 80, select the student for the scholarship.

11.Display the list of scholarship-eligible students.

12.Stop.


**5. Time Complexity**

O(n log n)

Where n is the number of students.

The main operation is sorting the students according to their marks. Sorting takes O(n log n) time.

After sorting, the program checks each student for scholarship eligibility, which takes O(n) time.

Therefore, the overall time complexity is:

O(n log n)
