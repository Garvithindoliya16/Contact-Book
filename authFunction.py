import getpass
from colorama import Fore
import os
AUTH_FILE = "auth.txt"


# ------------------ Authentication ------------------
def setup_password():
    print(Fore.CYAN+"No password found. Please set up a new password.")
    while True:
        pwd = getpass.getpass("Set Password: ").strip()
        confirm_pwd = getpass.getpass("Confirm Password: ").strip()
        if not pwd:
            print(Fore.RED+"Password cannot be empty!")
        elif pwd != confirm_pwd:
            print(Fore.RED+"Passwords do not match! Try again.")
        else:
            with open(AUTH_FILE, "w") as f:
                f.write(pwd)
            print(Fore.GREEN+"Password set successfully!\n")
            return


def verify_password():
    if not os.path.exists(AUTH_FILE):
        setup_password()

    with open(AUTH_FILE, "r") as f:
        saved_pwd = f.read().strip()



    attempts = 3
    while attempts > 0:
        pwd = getpass.getpass("Enter Password: ").strip()
        if pwd == saved_pwd:
            print(Fore.GREEN+"Access Granted!\n")
            return True
        else:
            attempts -= 1
            print(Fore.RED+f"Incorrect password! Attempts left: {attempts}")
    print(Fore.RED+"Too many failed attempts. Exiting...")
    exit()