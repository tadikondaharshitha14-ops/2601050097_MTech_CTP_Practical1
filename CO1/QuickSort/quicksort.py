# Hospital Patient Priority System
# Using Quick Sort

def quick_sort(patients):

    if len(patients) <= 1:
        return patients

    # Select last patient as pivot
    pivot = patients[-1]

    higher = []
    lower = []
    equal = []

    # Partition the patients
    for patient in patients:

        if patient[1] > pivot[1]:
            higher.append(patient)

        elif patient[1] < pivot[1]:
            lower.append(patient)

        else:
            equal.append(patient)

    # Recursively sort
    return quick_sort(higher) + equal + quick_sort(lower)


# Main Program

patients = []

print("===== HOSPITAL PATIENT PRIORITY SYSTEM =====")

n = int(input("Enter number of patients: "))

# Input patient details
for i in range(n):

    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    priority = int(input("Enter priority/severity score: "))

    patients.append((name, priority))


# Display original list
print("\n--- ORIGINAL PATIENT LIST ---")

for name, priority in patients:
    print(name, "-", priority)


# Apply Quick Sort
sorted_patients = quick_sort(patients)


# Display sorted patients
print("\n--- PATIENTS SORTED BY PRIORITY ---")

for name, priority in sorted_patients:
    print(name, "-", priority)


# Display highest priority patient
if len(sorted_patients) > 0:

    print("\n--- HIGHEST PRIORITY PATIENT ---")
    print("Patient:", sorted_patients[0][0])
    print("Priority Score:", sorted_patients[0][1])


print("\nProgram ended.")
