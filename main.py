import time
from config import *                                        # Import Login ID & Password Configuration
from VPN.windscribe import Windscribe                       # Import Windscribe Script

Windscribe = Windscribe(login, password)                    # Authorize the Login ID & Password



def start_pro():                                                    # Takes Input for Create Tunnels
    n = input("Number of Tunnels :")
    num = int(n)
    condition_stmt(num)


def condition_stmt(num):                                            # Check Input is Valid or Not
    if num>0 and num<1000:
        tunnel_loop(num)
        countdown()
        output_print()
    else:
        print("\nInvalid choice. Range of Tunnels is 1 to 999")


def tunnel_loop(num):                                               # Create a loop for Multiple Time Execution
    for i in range(1,num+1):
        print(f"\nTunnel No. {i}")
        Windscribe.connect(rand=True)
        countdown2()
        print("\n")


def countdown():                                                    # Show the Countdown Before Disconnect the Tunnel
    t = 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Tunnel Will Disconnecting in {timer} sec", end="\r")
        time.sleep(1)
        t -= 1
    
def countdown2():                                                   # Show the countdown before connecting ti next Tunnel
    t = 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"New Tunnel Creating in {timer} sec", end="\r")
        time.sleep(1)
        t -= 1


def output_print():                                               # sDisconnect the Tunnels
    print("\n")
    Windscribe.disconnect()
    print("\nTunnel is Disconnected")





start_pro()                                                         # First Function

print("\nThanks for Using Hidden ID Project\n")