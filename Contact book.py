contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    query = input("Search by name or phone: ")
    results = [contact for contact in contacts
        if query.lower() in contact["name"].lower() or query in contact["phone"]]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, "
                  f"Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.\n")

def update_contact():
    query = input("Enter name or phone of contact to update: ")
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query == contact["phone"]:
            print("Leave blank to keep the current value.")
            name = input(f"New name [{contact['name']}]: ") or contact["name"]
            phone = input(f"New phone [{contact['phone']}]: ") or contact["phone"]
            email = input(f"New email [{contact['email']}]: ") or contact["email"]
            address = input(f"New address [{contact['address']}]: ") or contact["address"]
            contact.update({
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    query = input("Enter name or phone of contact to delete: ")
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query == contact["phone"]:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.remove(contact)
                print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thanks for using the Contact Book! Goodbye!")
            break
        else:
            print("Please choose a valid option (1-6).\n")

if __name__ == "__main__":
    main()
    


