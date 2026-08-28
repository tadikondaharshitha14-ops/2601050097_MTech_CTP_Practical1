**Student Attendance System**

**1. Objective**

To develop a Python-based attendance analysis system that calculates the attendance percentage of multiple students and generates an attendance report.


**2. Input**

**The program accepts:**

1.Number of students

2.Student name

3.Number of classes attended

4.Total number of classes conducted


**3. Output**

**The program displays:**

1.Attendance percentage of each student

2.Attendance status

3.Below 75%

4.Eligible

5.Student with the highest attendance

6.Class average attendance

7.List of students whose attendance is below 75%


**4. Algorithm**

1.Start.

2.Create an empty list to store student details.

3.Read the number of students.

4.For each student:

Read the student's name.

Read the number of classes attended.

Read the total number of classes conducted.

Calculate the attendance percentage using: Attendance Percentage = (Classes Attended / Total Classes Conducted) × 100
Store the student details and calculated percentage in the list.

Display the attendance percentage and status of each student.

Find the student with the highest attendance by comparing the attendance percentages.

Calculate the class average attendance by adding all attendance percentages and dividing by the number of students.

Display the highest attendance and class average.

Check each student's attendance percentage.

Display the students whose attendance is below 75%.

If no student has attendance below 75%, display an appropriate message.

5.Stop.


**5. Time Complexity**

O(n)

Where n is the number of students.

The program performs several separate loops over the list of students. 

Since these loops run sequentially, the overall time complexity remains O(n).
