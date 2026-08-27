# Maximum Agricultural Profit
# Using Kadane's Algorithm

profits = [-100, 200, 300, -50, 400, -200]

max_sum = profits[0]
current_sum = profits[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(profits)):

    if profits[i] > current_sum + profits[i]:
        current_sum = profits[i]
        temp_start = i
    else:
        current_sum = current_sum + profits[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

print("Daily Profit/Loss:")
print(profits)

print("\nMaximum Continuous Profit:", max_sum)

print("Best Profitable Period:")

for i in range(start, end + 1):
    print(profits[i], end=" ")

print("\n")
print("Calculation:")

for i in range(start, end + 1):
    if i > start:
        print("+", end=" ")
    print(profits[i], end=" ")

print("=", max_sum)

