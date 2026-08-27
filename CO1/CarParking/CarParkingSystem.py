TOTAL_SLOTS = 100
RATE_PER_HOUR = 20

parking = {}

while True:

    print("\n--- PARKING MANAGEMENT SYSTEM ---")
    print("1. Show Available Slots")
    print("2. Park Vehicle")
    print("3. Release Vehicle")
    print("4. Calculate Parking Charge")
    print("5. Show Parking Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Show Available Slots
    if choice == 1:

        available_slots = TOTAL_SLOTS - len(parking)

        print("\n--- PARKING AVAILABILITY ---")
        print("Total Slots:", TOTAL_SLOTS)
        print("Occupied Slots:", len(parking))
        print("Available Slots:", available_slots)

        if available_slots == 0:
            print("Parking is FULL!")

    # 2. Park Vehicle
    elif choice == 2:

        if len(parking) == TOTAL_SLOTS:
            print("\nParking is FULL!")
            print("No slots are available.")

        else:
            vehicle = input("Enter vehicle number: ")

            if vehicle in parking.values():
                print("Vehicle is already parked.")

            else:
                for slot in range(1, TOTAL_SLOTS + 1):

                    if slot not in parking:
                        parking[slot] = vehicle

                        print("Vehicle", vehicle,
                              "parked in Slot", slot)
                        break

    # 3. Release Vehicle
    elif choice == 3:

        vehicle = input("Enter vehicle number to release: ")

        found = False

        for slot, parked_vehicle in list(parking.items()):

            if parked_vehicle == vehicle:

                del parking[slot]

                print("Vehicle", vehicle, "has left the parking area.")
                print("Slot", slot, "is now available.")

                found = True
                break

        if not found:
            print("Vehicle not found.")

    # 4. Calculate Parking Charge
    elif choice == 4:

        vehicle = input("Enter vehicle number: ")

        found = False

        for slot, parked_vehicle in parking.items():

            if parked_vehicle == vehicle:

                hours = float(input("Enter parking hours: "))

                charge = hours * RATE_PER_HOUR

                print("\n--- PARKING BILL ---")
                print("Vehicle:", vehicle)
                print("Slot:", slot)
                print("Parking Hours:", hours)
                print("Rate Per Hour: ₹", RATE_PER_HOUR)
                print("Parking Charge: ₹", charge)

                found = True
                break

        if not found:
            print("Vehicle not found.")

    # 5. Show Parking Details
    elif choice == 5:

        print("\n--- PARKING DETAILS ---")

        if len(parking) == 0:
            print("Parking area is empty.")

        else:
            for slot, vehicle in parking.items():
                print("Slot", slot, ":", vehicle)

            print("Occupied Slots:", len(parking))
            print("Available Slots:",
                  TOTAL_SLOTS - len(parking))

    # 6. Exit
    elif choice == 6:

        print("\nProgram ended.")
        break

    # Invalid Choice
    else:

        print("Invalid choice.")
