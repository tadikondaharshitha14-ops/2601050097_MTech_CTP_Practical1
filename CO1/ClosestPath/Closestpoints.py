import math

# Nearest Taxi Finder

# Customer location
customer_x = 10
customer_y = 10

# Taxi details
taxis = {
    "Taxi A": (2, 3),
    "Taxi B": (11, 12),
    "Taxi C": (25, 30)
}

nearest_taxi = None
minimum_distance = float("inf")

print("===== NEAREST TAXI FINDER =====")

print("\nCustomer Location:")
print("(", customer_x, ",", customer_y, ")")

print("\n--- TAXI DISTANCES ---")

# Calculate distance for each taxi
for taxi, location in taxis.items():

    taxi_x = location[0]
    taxi_y = location[1]

    # Euclidean distance formula
    distance = math.sqrt(
        (taxi_x - customer_x) ** 2 +
        (taxi_y - customer_y) ** 2
    )

    print(taxi, "-> Distance:", round(distance, 2))

    # Find nearest taxi
    if distance < minimum_distance:
        minimum_distance = distance
        nearest_taxi = taxi


# Display nearest taxi
print("\n--- NEAREST TAXI ---")
print("Nearest Taxi:", nearest_taxi)
print("Distance:", round(minimum_distance, 2))

print("\nTaxi", nearest_taxi, "is closest to the customer.")
