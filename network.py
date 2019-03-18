# !/usr/bin/python3
import os
import socket
import webbrowser
import urllib.request
import string

def network():

    print("\nVersion: 1.3")
    print("\nMade by @upn or bypass#0666")
os.system('clear')
print("""_____________________________________
|                                   |
|                                   |
|         NETWORK ANALYSIS          |
|                                   |
|   Made by bypass in Python 3.7    |
|___________________________________|
""")

sites = input("""
            (1) DNS Leak Test
            (2) What is my IP?
            (3) Tools to anonymize yourself
            (4) Tools for collecting information
            (5) Wipe screen
            (6) Exit
[NETWORK] $	""")

def getIP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        os.system('clear')
        print("Sending " + "'" + host_ip + ":" + host_name.title() + "'" + " back to their terminal session...")
    except:
        print("Exiting...")
def Clear():
    os.system('clear && python3 network.py');

if sites == '1':
    print("Opening Browser...")
    webbrowser.open("https://www.dnsleaktest.com")
    os.system('clear')
    print("Sending you to DNSLeakTest...")
if sites == '2':
    print("Retreiving User Info...")
    os.system('clear')
    IP = input("""What IP are you trying to look up?
        [Network.py] $ """)
    with urllib.request.urlopen("https://geoip-db.com/jsonp/" + IP) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")
        os.system('touch results.txt')
        with open(os.path.expanduser("~/Desktop/") + "results.txt", "w") as ip:
            ip.write(data)
            os.system('mv results.txt ~/Desktop/')
if sites == '3':
    print("Opening Browser...")
    webbrowser.open("https://thehackerstuff.com/top-5-best-tools-to-go-anonymous-online-using-tor-network/")
    os.system('clear')

if sites == '4':
    print("Opening Browser...")
    webbrowser.open("https://thehackerstuff.com/top-10-advanced-information-gathering-tools-for-linux-windows/")
    os.system('clear')

if sites == '5':
    Clear()
    print("Redirecting...")
    os.system('clear && python3 network.py')
if sites == '6':
    getIP()
