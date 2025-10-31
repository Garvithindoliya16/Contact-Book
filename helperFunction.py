import re
from colorama import Fore, Style
from utilityFunctions import save_contacts

#Validation Functions
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))


def contact_exists(contacts, name):
    return any(contact['name'].lower() == name.lower() for contact in contacts)

def phone_exists(contacts, phone):
    return any(contact['phone number'] == phone for contact in contacts)


def add_contact(contacts):
    name = input(Fore.CYAN+"Enter Name: ").strip()
    if not name:
        print(Fore.RED+"Name cannot be empty!\n")
        return
    if contact_exists(contacts, name):
        print(Fore.RED+"Contact with this name already exists!\n")
        return

    phone = input(Fore.CYAN+"Enter Phone Number (10 digits): ").strip()
    if not is_valid_phone(phone):
        print(Fore.RED+"Invalid phone number! It should be 10 digits.\n")
        return
    if phone_exists(contacts, phone):
        print(Fore.RED+"Contact with this Phone Number already exists!\n")
        return

    email = input(Fore.CYAN+"Enter Email: ").strip()
    if not is_valid_email(email):
        print(Fore.RED+"Invalid email format!\n")
        return

    address = input(Fore.CYAN+"Enter Address: ").strip()
    if not address:
        print(Fore.RED+"Address cannot be empty!\n")
        return

    contacts.append({
        "name": name,
        "phone number": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(Fore.GREEN+"CContact added successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print(Fore.RED+"No contacts found.\n")
        return
    sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())
    print(Style.BRIGHT + Fore.BLUE + "\nAll Contacts (Sorted Alphabetically):")
    print(Fore.MAGENTA+"-" * 80)
    for i, contact in enumerate(sorted_contacts, start=1):
        print(Fore.MAGENTA + f"{i}. {contact['name']} | {contact['phone number']} | {contact['email']} | {contact['address']}")
    print("-" * 80)


def search_contact(contacts):
    keyword = input(Fore.CYAN+"Enter name or phone to search: ").lower()
    found = [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone number']]
    if not found:
        print(Fore.RED+"No matching contacts found.\n")
        return
    print(Fore.GREEN+"\nSearch Results:")
    print("-" * 80)
    for c in found:
        print(f"{c['name']} | {c['phone number']} | {c['email']} | {c['address']}")
    print("-" * 80)


def update_contact(contacts):
    name = input(Fore.CYAN+"Enter the name of contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave a field blank to keep the same value.")
            new_phone = input(Fore.CYAN+f"Phone Number ({contact['phone number']}): ").strip()
            if new_phone and not is_valid_phone(new_phone):
                print(Fore.RED+"Invalid phone number!\n")
                return
            contact['phone number'] = new_phone or contact['phone number']

            new_email = input(Fore.CYAN+f"Email ({contact['email']}): ").strip()
            if new_email and not is_valid_email(new_email):
                print(Fore.RED+"Invalid email!\n")
                return
            contact['email'] = new_email or contact['email']

            new_address = input(Fore.CYAN+f"Address ({contact['address']}): ").strip()
            contact['address'] = new_address or contact['address']

            save_contacts(contacts)
            print(Fore.GREEN+"Contact updated successfully!\n")
            return
    print(Fore.RED+"Contact not found.\n")

def delete_contact(contacts):
    name = input(Fore.CYAN+"Enter the name of contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            confirm = input(Style.BRIGHT+Fore.RED+f"Are you sure you want to delete '{contact['name']}'? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(contact)
                save_contacts(contacts)
                print(Fore.GREEN+"Contact deleted successfully!\n")
            else:
                print(Fore.RED+"Deletion cancelled.\n")
            return
    print(Fore.RED+"Contact not found.\n")