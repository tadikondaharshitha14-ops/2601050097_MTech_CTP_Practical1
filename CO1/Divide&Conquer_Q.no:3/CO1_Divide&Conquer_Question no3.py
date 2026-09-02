# Merge Sort to find Maximum Temperature

def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result


# Temperature readings
temperatures = [32, 28, 35, 31, 39, 36, 30, 34]

# Sort the temperatures
sorted_temperatures = merge_sort(temperatures)

# Maximum temperature is the last element
maximum_temperature = sorted_temperatures[-1]

print("Temperature readings:", temperatures)
print("Sorted temperatures:", sorted_temperatures)
print("Maximum temperature:", maximum_temperature, "°C") 