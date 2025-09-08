no_of_years = int(input("Enter number of years: "))
total_no_of_months = 0
total_inches_of_rain = 0
average_inches_of_rain = 0
# Determine the season
for year in range(no_of_years):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for month in month_list:
        inches_of_rain = float(input(f"Enter inches of rain for month {month}: "))
        total_no_of_months += 1
        total_inches_of_rain += inches_of_rain

average_inches_of_rain = total_inches_of_rain / total_no_of_months if total_no_of_months > 0 else 0
print(f"Total months: {total_no_of_months}")
print(f"Total inches of rain: {total_inches_of_rain:.2f}")
print(f"Average inches of rain per month: {average_inches_of_rain:.2f}")
    
