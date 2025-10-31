import csv
import os

CONTACT_FILE="contacts.csv"
FIELDS = ["name", "phone number", "email", "address"]

def load_contacts():
    contacts = []
    if os.path.exists(CONTACT_FILE):
        try:
            with open(CONTACT_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                contacts = list(reader)
        except Exception as e:
            print(f"Error reading file: {e}")
    return contacts

def save_contacts(contacts):
    try:
        with open(CONTACT_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(contacts)
    except Exception as e:
        print(f"Error saving file: {e}")