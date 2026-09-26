def show_menu():
    print("\n=== Contact Manager ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print(f"Added: {name} → {phone}")

contacts = {}  # دفتر العناوين فاضي
def view_contacts():
    print("\n=== All Contacts ===")
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {name} → {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted: {name}")
    else:
        print(f"Contact '{name}' not found.")


def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")
    print("Contacts saved to file.")

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No saved contacts found. Starting fresh.")
        
contacts = {}
load_contacts()  # حمّل البيانات من الملف لو موجود     

while True:
    show_menu()
    choice = input("Choose option: ")
    
    if choice == "5":
        save_contacts()
        print("Goodbye!")
        break
    elif choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
         search_contact()
    elif choice == "4":
        delete_contact()
    else:
        print("Invalid choice, try again")