import helperFunction
from colorama import Fore, Style
from utilityFunctions import load_contacts
from authFunction import verify_password

verify_password()
contacts = load_contacts()

while True:
        print(Style.BRIGHT + Fore.MAGENTA + "\n===== CONTACT BOOK MENU =====")
        print(Fore.CYAN + """
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
""")
        choice = input(Fore.YELLOW + "Enter your choice (1-6): ").strip()

        if choice == '1':
            helperFunction.add_contact(contacts)
        elif choice == '2':
            helperFunction.view_contacts(contacts)
        elif choice == '3':
            helperFunction.search_contact(contacts)
        elif choice == '4':
            helperFunction.update_contact(contacts)
        elif choice == '5':
            helperFunction.delete_contact(contacts)
        elif choice == '6':
            print(Fore.GREEN + "Exiting Contact Book. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again.\n")