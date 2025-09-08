#create a contact list using name and phone number. Also append a new contact to the list, remove a contact, and display the contact list.
contact_list = []
def add_contact(name, phone):
    contact_list.append({"name": name, "phone": phone})
def remove_contact(name):
    global contact_list
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            break
def display_contacts():
    if not contact_list:
        print("No contacts available.")
    else:
        print("Contact List:")
        for contact in contact_list:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
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