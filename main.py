import subprocess
import os

title='\nIntuitive Network Analysis Tool'
print(title)

def install_assets():
    os.system("sudo apt-get install nload")
    os.system("sudo apt-get install nmap")
    os.system("sudo apt install inetutils-traceroute")
    os.system("sudo apt install ethtool")

def path_time_to_website():
    website = input("Please enter a valid website (ex. www.google.com) : \n")
    os.system("traceroute "+website)

def shut_down_all_networking():
    print(">> Shutting down networking interface...")
    os.system("systemctl stop NetworkManager")

def start_up_all_networking():
    print(">> Starting up networking interface...")
    os.system("systemctl start NetworkManager")

def list_devices():
	print(">> thinking...")
	cmd = "hostname -I"
	ip = os.popen(cmd).read().split(' ')[0]
	os.system("sudo nmap "+ip+"/24 | grep MAC")

def network_data_usage():
	os.system("nload")

def list_ports():
	os.system("ss -a -t | less")

response = ""
while(response != "quit" and response != "q"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("What would you like to do?\n")
    print("0) Install required assets.")
    print("1) List devices on your network.")
    print("2) Show network data usage for your computer.")
    print("3) Show active network ports for your computer.")
    print("4) Find the path time for a website.")
    print("5) Stop all networking.")
    print("6) Start all networking.")
    print("\nUse CTRL+C or type 'quit' to exit.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    response = input("Choose an option from the list above:\n")

    if response == "0":
        install_assets()

    if response == "1":
        list_devices()

    if response == "2":
        network_data_usage()

    if response == "3":
        list_ports()

    if response == "4":
        path_time_to_website()

    if response == "5":
        shut_down_all_networking()

    if response == "6":
        start_up_all_networking()

    if response == "q" or response == "quit":
        print(">> exiting...")
    else:
        print("Please enter a valid command.\n")



