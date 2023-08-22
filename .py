import time
from datetime import datetime as dt
import os

sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host if os.name == 'posix' else Window_host

redirect = "127.0.0.1"

def block_websites(start_hour, end_hour):
    while True:
        try:
            current_time = dt.now()
            start_time = dt(current_time.year, current_time.month, current_time.day, start_hour)
            end_time = dt(current_time.year, current_time.month, current_time.day, end_hour)

            if start_time <= current_time <= end_time:
                print("Do the work ...")
                with open(default_hoster, "r+") as hostfile:
                    hosts = hostfile.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            hostfile.write(redirect + " " + site + "\n")
            else:
                with open(default_hoster, "r+") as hostfile:
                    hosts = hostfile.readlines()
                    hostfile.seek(0)
                    for host in hosts:
                        if not any(site in host for site in sites_to_block):
                            hostfile.write(host)
                    hostfile.truncate()
                print("Good Time")
            
            time.sleep(3)
            
        except PermissionError as e:
            print(f"Caught a permission error: Try Running as Admin {e}")
            time.sleep(10)  # Delay and retry

if __name__ == "__main__":
    block_websites(9, 21)
