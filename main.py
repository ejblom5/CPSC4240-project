import subprocess
import os

title='Intuitive Network Analysis Tool'
print(title)

def install_assets():
    os.system("sudo apt-get install nload")
    os.system("sudo apt-get install nmap")
def network_data_usage():
    os.system("nload")

def list_devices():
    print("thinking...")
    cmd = "hostname -I"
    ip = os.popen(cmd).read().split(' ')[0]
    os.system("sudo nmap "+ip+"/24 | grep MAC")

response = ""
while(response != "quit"):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("What would you like to do?")
    print("0) Install required assets")
    print("1) List devices on your network")
    print("2) Show network data usage for your computer (use CTRL+C to exit)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    response = input("Choose an option from the list above or enter 'quit' to exit: ")

    if response == "0":
        install_assets()
    if response == "1":
        list_devices()
    if response == "2":
        network_data_usage()
