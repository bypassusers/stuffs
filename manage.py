#!/usr/var/python3
#Made by @upn or bypass#0666
import shelve
import random
import os

def main():
    def greeting():
        print("Hello. Welcome to Manager.py. Passing you to the Main Screen...")

def manual():
    #Manually input a password
        print("\n")
        account = input("Account: ")
        username = input("Username: ")
        password = input("Password: ")
        entry = finish_new_account(account, password, username)
        open(os.path.expanduser("~/Desktop/") + "acc.dat", "w")
        print (entry + '\n')
        os.system('python3 manage.py')

def ClearScreen():
    os.system('clear && python3 manage.py')

def Pass():
    os.system('clear && python3 Pass.py')
def pinger():
    os.system('clear && python3 ping.py')

def find_account():
    """Find an existing account"""
    print ('\n')
    search = input("For which account are you searching: ")
    f = shelve.open("acc.dat")
    if search in f:
       account = f[search]
       print (account)
    else:
        print ("I'm sorry we could not find any account related to " + search)
    print ("\n")
    f.close()

def finish_new_account(account, password, username):
    """Sends entry to save() and returns a message"""
    entry = create_entry(account, password, username)
    save(account, entry)
    return "Save successful. " + "\n" + str(entry) + "\n"


def create_entry(account, password, username):
    """Creates the entry"""
    return "Account: " + account + " - Username: " + username + " - Password: " + password


def save(account, entry):
    """Saves account"""
    f = shelve.open("acc.dat")
    saves = [entry]
    f[account] = saves
    f.sync()
    f.close()


def delete_account():
    """Deletes an account"""
    print('\n')
    account = input("What account do you want to delete?: ")
    f = shelve.open("acc.dat")
    if account in f:
        confirm_deletion = input("Delete: " + account + "? Y/N: ")
        if confirm_deletion.lower() in ('yes', 'y', ' '):
            del f[account]
            print ("This account has been deleted")
        else:
            print("Canceled... ")
    else:
        print ("I'm sorry we could not find any account related to " + account)
    print('\n')
    f.close()


def all_accounts():
    """prints all accounts: A hidden command"""
    f = shelve.open("acc.dat")
    klist = f.keys()
    f.close()
    print (klist)
    print ("\n")


def gen_password(digits_in_pass):
    """Returns a randomly generated password"""
    alphanumeric_chars = ["0123456789",
                          "abcdefghijklmnopqrstuvwxyz",
                          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    return make_password(digits_in_pass, *alphanumeric_chars)


def make_password(length, *collections_of_characters):
    """Creates a random password"""
    characters = set()
    for collection in collections_of_characters:
         characters.update(str(c) for c in collection)
    characters = list(characters)

    password = [random.choice(characters) for _ in range(0, length)]
    return "".join(password)
def ExitTerm():
    os.system('exit')

def program_start():
    """MAIN"""
    os.system('clear')
    print("""
____________________________________________________________________________________________________________________________________________
|                                                                                                                                          |
|                                                                                                                                          |
|                                                        BYPASS's PASSWORD MANAGER                                                         |
|                                                                                                                                          |
|__________________________________________________________________________________________________________________________________________|
                                          Made compatiable with Python3.x by @upn or bypass#0666
                                       """)
    choice = ""
    if choice != '4':
        os.system('exit')
    choice = input("""
     (1) Manually input an account
     (2) Search for an existing account
     (3) Delete an account
     (4) Clear your Screen
     (5) Go to Password Generator
     (6) Go to Pinger
     (7) Go to Self Network Analysis
     (8) Exit
[MANAGE] $ """)
    if choice == "1":
            manual()
    elif choice == "2":
            find_account()
    elif choice == "3":
            delete_account()
    elif choice == "4":
            ClearScreen()
    elif choice == "5":
        os.system('python3 main.py')
    elif choice == "all accounts":
            all_accounts()
    elif choice == "7":
        import network
        network.network()
    elif choice == "6":
        pinger()
    elif choice == "8":
        ExitTerm()
    else:
            print (" ")
program_start()
