import time
from config import login, password
from VPN.windscribe import Windscribe

def start_pro():
    num = int(input("Number of Tunnels: "))
    if 0 < num < 1000:
        tunnel_loop(num)
        countdown()
        output_print()
    else:
        print("\nInvalid choice. Range of Tunnels is 1 to 999")

def tunnel_loop(num):
    Windscribe = Windscribe(login, password)
    for i in range(1, num+1):
        print(f"\nTunnel No. {i}")
        Windscribe.connect(rand=True)
        countdown2()
        print("\n")

def countdown(t=60, message_prefix="Tunnel Will Disconnecting in"):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"{message_prefix} {timer} sec", end="\r")
        time.sleep(1)
        t -= 1

def output_print():
    print("\n")
    Windscribe.disconnect()
    print("\nTunnel is Disconnected")

start_pro()
print("\nThanks for Using Hidden ID Project\n")
