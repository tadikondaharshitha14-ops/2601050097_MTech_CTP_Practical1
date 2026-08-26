**Student Scholarship Selection System**

**1. Objective**

To develop a Python-based student scholarship selection system that stores student names and marks, sorts the students in descending order of marks, and identifies students who are eligible for a scholarship based on their marks.

For this problem, a student is eligible for a scholarship if the student scores 80 marks or above.


**2. Input**

**The program accepts:**

Number of students
Student name
Student marks
Scholarship eligibility mark

**3. Output**

**The program displays:**

List of students sorted in descending order of marks
Student names and their marks
Students eligible for the scholarship


**4. Algorithm**

Start.
Create a list to store student names and marks.
Read the number of students.
For each student:
Read the student's name.
Read the student's marks.
Store the name and marks in the list.
Sort the list of students in descending order of marks.
Display all students with their marks after sorting.
Set the scholarship eligibility mark to 80.
Check each student's marks.
If a student's marks are greater than or equal to 80, select the student for the scholarship.
Display the list of scholarship-eligible students.
Stop.


**5. Time Complexity**

O(n log n)

Where n is the number of students.

The main operation is sorting the students according to their marks. Sorting takes O(n log n) time.

After sorting, the program checks each student for scholarship eligibility, which takes O(n) time.

Therefore, the overall time complexity is:

O(n log n)
