#!/bin/python3
#-*- coding: latin -*-

import string
import random
import os
import sys
#MADE BY: @snms or bypass#0666

os.system('clear')

def socialMedia():
        print("""
    _____________________________________________________________________
    |                                                                   |
    |                                                                   |
    |  @snms or 'bypass' made this Password Generator in Python 3.7 :D  |
    |                                                                   |
    |___________________________________________________________________|
            """)

def printMenu(arg = ""): #prevents repeating code (even though the design was different) function to print a menu with arguments to add extra menu info
    os.system('clear')   #clear the console
    print("""
___________________________________________________________________________________________
|                                                                                         |
|   $$$$$$$\                                                                       $$\    |
|   $$  __$$\                                                                      $$ |   |
|   $$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\ $$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$$ |   |
|   $$$$$$$  |\____$$\ $$  _____|$$  _____|$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  __$$ |   |
|   $$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\  $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |   |
|   $$ |     $$  __$$ | \____$$\  \____$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |   |
|   $$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |   |
|   \__|      \_______|\_______/ \_______/  \_____\____/  \______/ \__|       \_______|   |
|                                                                                         |
|_________________________________________________________________________________________|
""" + arg)               #append our own string to the end if needed (optional since we set arg = "" in the arguements which defaults to "" if nothing is set)

printMenu("| ***Welcome to snms's Password Generator. Please wait as I assemble your password :)***  |\n[#########################################################################################]")
choice = input("""
Please Choose an Option :: Version 1.3 :: Contact Bypass for upadtes
	(1) Send me to the fucking generator already
	(2) Who made this?
	(3) Social Media & Contact
	(4) Quit
        (5) Pinger
        (6) Password Manager
        (7) Self Network Analysis
[MAIN] $ """)

if choice == '1':        #the issue here was the indentation. Python cares dearly about this. an indent is 4 spaces. You can't use TAB without changing it to 4 spaces per TAB
    printMenu("***THIS IS THE MAIN PART OF THE PASSWORD GENERATOR PLEASE ENTER AN AMOUNT***")
    choice = input("Enter an amount; dickhead: ")
    output = ""
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV0123456789!@#$%^&*()';:\|+-/''"
    for i in range(int(choice)): #cast the user input to an integer (this can crash if they enter letters)
        next_index = random.randrange(len(char))
        output = output + char[next_index]

    with open(os.path.expanduser("~/Desktop/") + 'pwd.txt', "w") as file:
        file.write(output)

print("""________________________________________________________________
|  Creating text file...                                       |
|  Creating Password Data...                                   |
|  Copying Password Data...                                    |
|  Transferring Data to text file...                           |
|  ...Done! your password has been created inside of 'pwd.txt' |
|______________________________________________________________|
""")

if choice == '3':      #If User picks choice 3
    os.system('clear')
    print("_______________")
    print("|_Version 1.3_|")
    socialMedia()
    print("""
____________________________
|                          |
|     @snms on twitter     |
| This is my discord user  |
| ------> bypass#0666      |
| XMPP: bypass@dismail.de  |
|__________________________|
\n""")
os.system('exit')

#how to name things:
#variables start with a lower case letter than every word after starts with a capital
#functions are the same but with an uppercase first letter

#stupidVariable = ""
#FunctionNameHere()
if choice == '2':
    print("Who made this? :: Version: 1.3")
    os.system('clear')
    print("""
_____________________________________________________________________
|                                                                   |
|                                                                   |
|  @snms or 'bypass' made this Password Generator in Python 3.7 :D  |
|                                                                   |
|___________________________________________________________________|
        """)
    print("\n")

if choice == '4':
    os.system('clear')
#     print("""
# [#########################################################################################################]
# | ╦═╗┌─┐┌┬┐┬ ┬┬─┐┌┐┌┬┌┐┌┌─┐  ┬ ┬┌─┐┬ ┬  ┌┬┐┌─┐  ┬ ┬┌─┐┬ ┬┬─┐  ┌┬┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐┬    ┌─┐┌─┐┌─┐┌─┐┬┌─┐┌┐┌ |
# | ╠╦╝├┤  │ │ │├┬┘││││││││ ┬  └┬┘│ ││ │   │ │ │  └┬┘│ ││ │├┬┘   │ ├┤ ├┬┘│││││││├─┤│    └─┐├┤ └─┐└─┐││ ││││ |
# | ╩╚═└─┘ ┴ └─┘┴└─┘└┘┴┘└┘└─┘   ┴ └─┘└─┘   ┴ └─┘   ┴ └─┘└─┘┴└─   ┴ └─┘┴└─┴ ┴┴┘└┘┴ ┴┴─┘  └─┘└─┘└─┘└─┘┴└─┘┘└┘ |
# [#########################################################################################################]""")


print("""
Returning you to your terminal session...

Destroying stored password data...
Destroying stored password data...
Compressing...
Thank you for using bypass password generator! """)
print("\n")
if choice == '5':
  import ping
  ping.main()
if choice == '6':
  import manage
  manage.main()
if choice == '7':
    import network
    network.network()
if choice == 'c' 'C':
    raise SystenExit
