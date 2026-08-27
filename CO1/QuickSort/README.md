**Hospital Patient Priority System**

**1. Objective**

To develop a Python-based Hospital Patient Priority System that arranges patients according to their priority or severity score in descending order. Patients with higher priority scores are displayed first.

Note: This is a sorting example for learning Quick Sort. Real hospital triage systems use medically validated clinical rules rather than a simple numerical score.


**2. Input**

**The program accepts:**

Number of patients

Patient name

Patient priority/severity score


**3. Output**

The program displays the patients arranged in descending order of priority score.

The patient with the highest priority score is displayed first.


**4. Algorithm**

1.Start.

2.Create a list to store patient names and priority scores.

3.Read the number of patients.

4.For each patient:

Read the patient name.

Read the priority/severity score.

5.Store the patient details in the list.

6.Select a pivot element.

7.Divide the patients into two groups:

Patients with scores greater than the pivot.

Patients with scores smaller than the pivot.

Recursively apply Quick Sort to both groups.

Combine the sorted groups and the pivot.

8.Display the patients in descending order of priority score.

9.Stop.


**5. Time Complexity**

Average Case: O(n log n)

Where n is the number of patients.

Quick Sort divides the list into smaller partitions and recursively sorts them. On average, the list is divided reasonably evenly, resulting in O(n log n) time complexity.
