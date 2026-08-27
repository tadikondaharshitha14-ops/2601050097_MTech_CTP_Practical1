**Parking Management System**


**1. Objective**

To develop a Python-based Parking Management System for a parking area with 100 parking slots. The system manages vehicle parking by showing available slots, allocating a slot to a vehicle, releasing the slot when a vehicle leaves, calculating parking charges, and identifying when the parking area is full.


**2. Input**

**The program accepts:**


Menu choice

Vehicle number

Parking duration in hours

Parking charge per hour

**The menu options are:**


1 – Show Available Slots
2 – Park Vehicle
3 – Release Vehicle
4 – Calculate Parking Charge
5 – Exit


**3. Output**


**The program displays:**


Number of available parking slots
Allocated parking slot for a vehicle
Vehicle and slot details
Released parking slot
Parking charge
Message when parking is full
Message when a vehicle is not found
Program exit message

The parking charge is calculated using:

Parking Charge = Parking Hours × Rate Per Hour

The number of available slots is calculated using:

Available Slots = Total Slots − Occupied Slots


**4. Algorithm**


1.Start.

2.Set the total number of parking slots to 100.

3.Create an empty dictionary to store vehicle and parking slot details.

4.Display the parking system menu.


**Read the user's choice.**


**If the choice is 1:**

Count the occupied slots.
Calculate the number of available slots.
Display the available slots.
If no slots are available, display "Parking is FULL!".


**If the choice is 2:**

Check whether all 100 slots are occupied.
If the parking area is full, display "Parking is FULL!".
Otherwise, read the vehicle number.
Search for the first available slot.
Allocate the slot to the vehicle.
Store the vehicle and slot information.
Display the allocated slot.


**If the choice is 3:**

Read the vehicle number.
Search for the vehicle in the parking system.
If the vehicle is found:
Release the allocated slot.
Remove the vehicle from the parking system.
Display that the slot is now available.
If the vehicle is not found, display "Vehicle not found.".


**If the choice is 4:**

Read the vehicle number.
Search for the vehicle.
If the vehicle is found:
Read the parking duration.
Read the rate per hour.
Calculate the parking charge using:
Parking Charge = Parking Hours × Rate Per Hour
Display the calculated parking charge.
If the vehicle is not found, display an appropriate message.


**If the choice is 5:**

Display the exit message.
Stop the program.

If an invalid choice is entered, display "Invalid choice."

Repeat the menu until the user selects the Exit option.

5.Stop.


**5. Time Complexity**

O(n)

Where n is the number of parking slots.

The system may need to search through all parking slots when allocating or releasing a vehicle. Therefore, the worst-case time complexity is O(n).

Since the parking area contains a maximum of 100 slots, the maximum number of slots that need to be checked is 100.

Operation-wise Complexity
Operation	Time Complexity
Show Available Slots	O(n)
Allocate Slot	O(n)
Release Slot	O(n)
Calculate Parking Charge	O(1)
Check Parking Full	O(1) / O(n)*

*Depending on how the number of occupied slots is maintained. If the program directly maintains an occupied-slot counter, checking whether the parking is full is O(1).
