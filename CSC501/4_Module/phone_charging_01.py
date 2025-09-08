phone_battery = 25

def keep_charging():
    global phone_battery
    print(f"Charging... Battery at {phone_battery}%")
    phone_battery += 15

# Estimate max number of charges needed: from 25 to 100 in steps of 15 => max 6 iterations
for _ in range(10):  # use a safe upper bound
    if phone_battery >= 100:
        break
    keep_charging()

print("Phone fully charged!")
