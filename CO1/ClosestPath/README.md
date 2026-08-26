**Nearest Taxi Finder**

**1. Objective**

To develop a Python-based Nearest Taxi Finder System that identifies the taxi closest to a customer's location using the distance between their coordinates.

The system calculates the distance between the customer and each available taxi and selects the taxi with the minimum distance.


**2. Input**

**The program accepts:**

Customer's location (x, y)
Number of available taxis
Taxi name
Location of each taxi (x, y)
The distance between two points is calculated using:
Distance = √((x₂ - x₁)² + (y₂ - y₁)²)


**3. Output**

**The program displays:**

Distance between the customer and each taxi
Name of the nearest taxi
Distance of the nearest taxi from the customer


**4. Algorithm**

Start.
Read the customer's coordinates (x, y).
Read the number of available taxis.
Create a list to store taxi names and their coordinates.
For each taxi:
Read the taxi name.
Read the taxi's coordinates (x, y).
Calculate the distance between the customer and the taxi using:
Distance = √((x₂ - x₁)² + (y₂ - y₁)²)
Store the calculated distance.
Compare the distances of all available taxis.
Find the taxi having the minimum distance.
Display the distance of each taxi.
Display the name and distance of the nearest taxi.
Stop.


**5. Time Complexity**

O(n)

Where n is the number of available taxis.

The program calculates the distance for each taxi once and compares each distance to find the minimum.

Therefore, the overall time complexity is O(n).
