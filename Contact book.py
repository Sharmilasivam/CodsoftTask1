contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    contacts[name] = phone_number
    print("Contact added successfully!")

def display_contacts():
    print("List of saved contacts:")
    for name, phone_number in contacts.items():
        print(f"Name: {name}, Phone Number: {phone_number}")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        phone_number = input("Enter the new phone number: ")
        contacts[name] = phone_number
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main menu
while True:
    print("\nContact Book Program")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
