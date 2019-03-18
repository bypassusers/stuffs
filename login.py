#!/usr/bin/python3
#Made by @snms

import sys
import os

# import register

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def login():
    clear()
    print("""   |                                                     |
   |               (Crossing terminal sessions....)      |
   |                (Thank you for logging in....)       |
   |                         (\_______/)                 |
   |                         |(u)   (u)|                 |
   |                        (___o___o___)                |
   |                         /\V/\V/\V/\V                |
   |                       /             \               |
   |----------------------|---------------|---------------|
   |                      ()             ()              |
   |______________________VV_____________VV______________|
   |_____________________________________________________|
""")

#Credentials {"user": pass}
creds = {"bypass": 50000}


clear()
print("""   |                                                     |
   |        (Welcome...please enter your username here)  |
   |                         (\_______/)                 |
   |                         |(u)   (u)|                 |
   |                        (___o___o___)                |
   |                         /\V/\V/\V/\V                |
   |                       /             \               |
   |----------------------|---------------|--------------|
   |                      ()             ()              |
   |______________________VV_____________VV______________|
   |_____________________________________________________|
""")
users = input("""
___________________________________________________________________
|  _      ____   _____ _____ _   _    ______ ____  _____  __  __  |
| | |    / __ \ / ____|_   _| \ | |  |  ____/ __ \|  __ \|  \/  | |
| | |   | |  | | |  __  | | |  \| |  | |__ | |  | | |__) | \  / | |
| | |   | |  | | | |_ | | | | . ` |  |  __|| |  | |  _  /| |\/| | |
| | |___| |__| | |__| |_| |_| |\  |  | |   | |__| | | \ \| |  | | |
| |______\____/ \_____|_____|_| \_|  |_|    \____/|_|  \_\_|  |_| |
|                                                                 |
 Username: """)

clear()
print("""   |                                                     |
   |               (Please enter your password here)     |
   |                         (\_______/)                 |
   |                         |(u)   (u)|                 |
   |                        (___o___o___)                |
   |                         /\V/\V/\V/\V                |
   |                       /             \               |
   |----------------------|---------------|---------------|
   |                      ()             ()              |
   |______________________VV_____________VV______________|
   |_____________________________________________________|
""")

passwords = input("""
___________________________________________________________________
|  _      ____   _____ _____ _   _    ______ ____  _____  __  __  |
| | |    / __ \ / ____|_   _| \ | |  |  ____/ __ \|  __ \|  \/  | |
| | |   | |  | | |  __  | | |  \| |  | |__ | |  | | |__) | \  / | |
| | |   | |  | | | |_ | | | | . ` |  |  __|| |  | |  _  /| |\/| | |
| | |___| |__| | |__| |_| |_| |\  |  | |   | |__| | | \ \| |  | | |
| |______\____/ \_____|_____|_| \_|  |_|    \____/|_|  \_\_|  |_| |
|                                                                 |
 Password: """)
clear()

#if users in creds_user and passwords in creds_pass:
if creds in creds:
     login()
else:
    print("INVALID CREDENTIALS! YOU HAVE BEEN BANISHED!")
    register = input("Would you like to register? y/n: ")
    if register == 'y':
        def Register():
            print("What would you like your username to be?")
            usercreate = input("Username: ")
            passcreate = int(input("Password: "))
            usercreate.append(creds)
            passcreate.append(creds)
