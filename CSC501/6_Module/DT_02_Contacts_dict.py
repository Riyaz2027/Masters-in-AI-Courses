contact_dict = {}

def add_contact(name, phone):
    contact_dict[name] = phone

def remove_contact(name):
    if name in contact_dict:
        del contact_dict[name]

def display_contacts():
    if not contact_dict:
        print("No contacts available.")
    else:
        print("Contact List:")
        for name, phone in contact_dict.items():
            print(f"Name: {name}, Phone: {phone}")

# Main program
while True:
    print("\nContact List Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Display Contacts")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
        print(f"Contact {name} added.")
    elif choice == '2':
        name = input("Enter the name of the contact to remove: ")
        remove_contact(name)
        print(f"Contact {name} removed.")
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")