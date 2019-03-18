import os
import time

def Clear():
    o = os
    if o.name == 'nt':
        o.system('cls')
    else:
        o.system('clear')

def main():
    print ("\nPinger made by bypass#0666 or @upn\n")

print ("""
____________________________________________________________________________________________________________________________________________
|                                                                                                                                          |
|                                                                                                                                          |
|                                                        BYPASS's PYTHON IP PINGER                                                         |
|                                                                                                                                          |
|__________________________________________________________________________________________________________________________________________|
                                               Made with Python3.7 by @upn or bypass#0666
""")
Clear()
host = input("""Enter The IP Address
[PING] $ """)
#What the IP of the recipient is
pings = input("""How many pings do you want?
[PING] $ """)
resp = os.system("ping -c" + pings + " " + host)
if resp == 0:
    print ("\n" "[" + host + "]" "\n\nIS STILL UP")
else:
    print ("\n" + "[" + host + "]" "\n\nIS FUCKING GONE")
    os.system('exit')
