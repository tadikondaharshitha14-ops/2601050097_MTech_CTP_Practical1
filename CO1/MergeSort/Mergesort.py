# Student Marks Ranking using Merge Sort

def merge_sort(students):

    # Base condition
    if len(students) <= 1:
        return students

    # Find middle
    mid = len(students) // 2

    # Divide the list into two halves
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare marks and arrange in descending order
    while i < len(left) and j < len(right):

        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Main Program

students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Arun", 68),
    ("Sneha", 95),
    ("Kiran", 78)
]

print("===== STUDENT MARKS RANKING =====")

print("\n--- ORIGINAL STUDENT LIST ---")

for name, marks in students:
    print(name, "-", marks)


# Apply Merge Sort
sorted_students = merge_sort(students)


print("\n--- STUDENTS SORTED BY MARKS ---")

for name, marks in sorted_students:
    print(name, "-", marks)


print("\n--- TOP STUDENT ---")

print("Student:", sorted_students[0][0])
print("Marks:", sorted_students[0][1])

print("\nProgram ended.")
