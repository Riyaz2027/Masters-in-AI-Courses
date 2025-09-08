# Take input from User
month = input("Enter month (e.g., March): ")
day = int(input("Enter day: "))

# Determine the season
if (month == "March" and day >= 20) or (month in ["April", "May"]) or (month == "June" and day <= 20):
    season = "Spring"
elif (month == "June" and day >= 21) or (month in ["July", "August"]) or (month == "September" and day <= 21):
    season = "Summer"
elif (month == "September" and day >= 22) or (month in ["October", "November"]) or (month == "December" and day <= 20):
    season = "Autumn"
else:
    season = "Winter"

print(f"{month} {day} is in {season}.")
