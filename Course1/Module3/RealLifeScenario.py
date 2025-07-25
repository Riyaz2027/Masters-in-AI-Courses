shoppingList = {'costco': ['milk', 'egg', 'cheese'],'walmart': ['detergent', 'towel', 'medicine']}
print('walmart shopping list', shoppingList['walmart'])
print('costco shopping list', shoppingList['costco'])
print('I have a situation where i bought detergent from costco so i need to remove from walmart list')
shoppingList['walmart'].remove('detergent')
print('but i forgot to buy cheese from costco so i am buying from walmart')
shoppingList['walmart'].append('cheese')
print('walmart shopping list', shoppingList['walmart'])
shoppingList['costco'].remove('cheese')
print('costco shopping list', shoppingList['costco'])

print('case 2 I want to remember the birthdays')
# Tuple of (name, birthday) pairs
birthdays_tuple = (
    ("John", "Jan 01 1987"),
    ("Joey", "Mar 03 1989"),
    ("Jimmy", "May 05 1999")
)
print(birthdays_tuple)
print('I am using tuple because it is not going to change')
print('a baby born and want to add it to the tuple')
birthdays_tuple = ('Jill','June 06 2020'), *birthdays_tuple
print(birthdays_tuple)

print('case 3 I want to remember the phone numbers of my friends')
# Dictionary of name and phone number pairs
phone_numbers = {
    "John": "860-456-7890",
    "Joey": "860-567-8901",
    "Jimmy": "860-678-9012"
}
print(phone_numbers)
print('I am using dictionary because I want to remember the phone numbers of my friends')
print('I want to add a new friend')
phone_numbers["Jill"] = "860-789-0123"
print(phone_numbers)