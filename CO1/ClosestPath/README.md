**Nearest Taxi Finder**

**1. Objective**

To develop a Python-based Nearest Taxi Finder System that identifies the taxi closest to a customer's location using the distance between their coordinates.

The system calculates the distance between the customer and each available taxi and selects the taxi with the minimum distance.


**2. Input**

**The program accepts:**

1.Customer's location (x, y)

2.Number of available taxis

3.Taxi name

4.Location of each taxi (x, y)

5.The distance between two points is calculated using:

6.Distance = √((x₂ - x₁)² + (y₂ - y₁)²)


**3. Output**

**The program displays:**

1.Distance between the customer and each taxi

2.Name of the nearest taxi

3.Distance of the nearest taxi from the customer


**4. Algorithm**

1.Start.

2.Read the customer's coordinates (x, y).

3.Read the number of available taxis.

4.Create a list to store taxi names and their coordinates.

5.For each taxi:

Read the taxi name.

Read the taxi's coordinates (x, y).

Calculate the distance between the customer and the taxi using:

Distance = √((x₂ - x₁)² + (y₂ - y₁)²)

Store the calculated distance.

Compare the distances of all available taxis.

Find the taxi having the minimum distance.

Display the distance of each taxi.

Display the name and distance of the nearest taxi.

6.Stop.


**5. Time Complexity**

O(n)

Where n is the number of available taxis.

The program calculates the distance for each taxi once and compares each distance to find the minimum.

Therefore, the overall time complexity is O(n).
