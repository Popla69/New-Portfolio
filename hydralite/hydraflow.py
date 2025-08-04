import os
import time

def banner():
    print(r"""
██████   ██████  ██████  ██       █████
██   ██ ██    ██ ██   ██ ██      ██   ██
██████  ██    ██ ██████  ██      ███████
██      ██    ██ ██      ██      ██   ██
██       ██████  ██      ███████ ██   ██
                              by Popla69 | PoplaLogics v2.5
""")

def menu():
    print("\nChoose a module to run:\n")
    print("1. Subdomain Scanner")
    print("2. Recon Scout")
    print("3. Port Scanner")
    print("4. Vulnerability Lookup")
    print("5. Exit\n")

def run_module(choice):
    if choice == "1":
        os.system("python subscan.py")
    elif choice == "2":
        os.system("python recon_scout.py")
    elif choice == "3":
        os.system("python portscanner.py")
    elif choice == "4":
        os.system("python vulnscanner.py")
    elif choice == "5":
        print("Exiting PoplaLogics HydraFlow. Stay safe!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    banner()
    while True:
        menu()
        choice = input("Enter your choice (1–5): ")
        run_module(choice)
        input("\n[Press Enter to return to main menu]")  # Keeps result visible

if __name__ == "__main__":
    main()
