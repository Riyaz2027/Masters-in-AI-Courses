# Total capacity
seat_capacity = 40
standee_capacity = 12

# Counters
seated_passengers = 0
standing_passengers = 0
total_passengers = 0

# Board seated passengers using while loop
while seated_passengers < seat_capacity:
    seated_passengers += 1
    total_passengers += 1
    print(f"Passenger {total_passengers}: Seated ({seated_passengers}/{seat_capacity})")

print("All seats are filled.")

# Board standing passengers using for loop
for i in range(1, standee_capacity + 1):
    standing_passengers += 1
    total_passengers += 1
    print(f"Passenger {total_passengers}: Standing ({standing_passengers}/{standee_capacity})")

print("Bus is full with seated and standing passengers.")