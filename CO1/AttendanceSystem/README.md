**Parking Management System**


**1. Objective**
To develop a Python-based parking management system that manages parking slots, stores vehicle details, displays occupied and available slots, and calculates parking charges when a vehicle is removed.


**2. Input**

**The program accepts**:
Menu choice
Vehicle number
Number of parking hours
Parking rate per hour
The menu options are:

1 – Park Vehicle
2 – Show Parking
3 – Remove Vehicle & Calculate Charge
4 – Exit


**3. Output**

**The program displays:**

Assigned parking slot for a vehicle
Parking details of occupied slots
Number of available parking slots
Parking bill
Parking charge
Message when parking is full
Message when a vehicle is not found
Message for an invalid choice
Program termination message
The parking charge is calculated using:

Parking Charge = Parking Hours × Rate Per Hour


**4. Algorithm**

Start.

Set the total number of parking slots to 100.

Create an empty dictionary to store parking details.

Display the parking system menu.

Read the user's choice.


**If the choice is 1**:

Check whether all parking slots are occupied.
If the parking area is full, display an appropriate message.
Otherwise, read the vehicle number.
Search for the first available parking slot.
Store the vehicle number in the available slot.
Display the assigned slot number.


**If the choice is 2:**

Check whether the parking area is empty.
If empty, display an appropriate message.
Otherwise, display the slot number and vehicle number of all parked vehicles.
Calculate and display the number of available slots.


**If the choice is 3:**

Read the vehicle number to be removed.
Search for the vehicle in the parking dictionary.
If the vehicle is found:
Read the number of parking hours.
Read the rate per hour.
Calculate the parking charge using:
Parking Charge = Parking Hours × Rate Per Hour
Display the parking bill.
Remove the vehicle from the parking dictionary.
Display that the slot is now available.
If the vehicle is not found, display an appropriate message.


**If the choice is 4:**

Display the program termination message.
Stop the program.
If the user enters an invalid choice, display an appropriate error message.

Repeat the menu until the user chooses the Exit option.

Stop.


**5. Time Complexity**
O(n)

Where n is the number of parking slots.

The program searches through the parking slots when parking or removing a vehicle. It may need to check all n slots in the worst case. Therefore, the overall time complexity is O(n).

Since the system has a maximum of 100 parking slots, n ≤ 100.
