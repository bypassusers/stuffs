#!/usr/bin/python3
#Made by @snms

import os
import string
import urllib.request
import sys

def Clear():
    #Clearing lol
    o = os.system
    if os.name == 'nt':
        o('cls')
    else:
        o('clear')

def Exit():
    #Exit the session
    sys.exit(0)

def Holder():
    #Printing for the social media
    Clear()
    print("\n")
    print("""Twitter: @snms
Discord: bypass#6115
E-Mail for contact: Vulns@tuta.io""")
    print("\n")

def SocialMedia():
    #My social media
    Clear()
    answer = str(input("Do you want to view the developers social media?\n\nr00t@HTML > "))
    if answer == 'y':
        Holder()
    if answer == 'Y':
        Holder()
    if answer == 'Yes':
        Holder()
    if answer == 'No':
        Exit()
    if answer == 'no':
        Exit()
    if answer == 'n':
        Exit()
    if answer == 'N':
        Exit()
    if answer == '':
        Holder()
    if answer =='yes':
        Holder()

def HTTPS():
    #For https links

    Clear()
    my_url = str(input("What is the HTTPS link? e.g 'Paypal.com' or 'Amazon.com'\nr00t@HTML > "))
    ending = str(input("What is the ending of the website? e.g '.com' or '.net' (DO NOT PLACE A '.')\nr00t@HTML > "))
    url = urllib.request.urlopen("https://www." + my_url + "." + ending)
    for lines in url.readlines():
        print(lines)


def HTTP():
    #For http links
    Clear()
    my_url = str(input("What is the HTTP link of the website?\n\nr00t@HTML > "))
    ending = str(input("What is the ending of the website? e.g '.com' or '.net'\n\nr00t@HTML > "))
    http_url = urllib.request.urlopen("http://www." + my_url + ending)
    for lines in url.readlines():
        print(lines)

# To go to either HTTPS or HTTP functions
def Intermission():
    Clear()
    which_one = str(input("Is your website you're trying to pull HTML from HTTPS or HTTP?\nr00t@HTML > "))
    if which_one == 'HTTP':
        HTTP()
    if which_one == 'http':
        HTTP()
    if which_one == 'HTTPS':
        HTTPS()
    if which_one == 'https':
        HTTPS()

def Menu():
    Clear()
    option = str(input("""What would you like to view?
    _________________________________________________
                   |
                   L[   Pull   ]
                   |
                   L[   Social ]
                   |
                   L[   Exit   ]

    r00t@HTML > """))

    if option == 'pull html':
        Intermission()

    if option == 'Pull HTML':
        Intermission()

    if option == 'Social':
        SocialMedia()

    if option == 'social':
        SocialMedia()

    if option == '':
        Clear()
        print("\n")
        print("Exiting...")
        print("\n")

    if option == 'pull':
        Intermission()

    if option == 'Pull':
        Intermission()

    if option == 'exit':
        Clear()
        print("\n")
        print("Exting...")
        print("\n")

    if option == 'Exit':
        Clear()
        print("\n")
        print("Exiting...")
        print("\n")

def run():
    Menu()

run()
